import serial
import threading
from time import sleep


class Display:

    def __init__(self, port, baudrate):
        try:
            self.serialCon = serial.Serial(port, baudrate)
            sleep(2)  # reset wenn Serial geöffnet wird
        except:
            print("Couldn't open Serial port")

        self.displayWidth = 0
        self.displayHight = 0
        self.mypixels = []
        self.__getDisplay()
        self.__readLines()

    def __readLines(self):
        readThread = threading.Thread(target=self.__readSer)
        readThread.isDaemon()
        readThread.start()

    def __readSer(self):
        while self.__checkSer():
            print(self.serialCon.readline())

    def __getDisplay(self):
        while self.__checkSer():
            self.__writeSer('ACK')
            if b'SOGENUGACK' in self.serialCon.readline():
                self.displayWidth = int(self.serialCon.readline().decode('utf-8')) - 1
                self.displayHight = int(self.serialCon.readline().decode('utf-8')) - 1
                break

    def __writeSer(self, msg):
        if self.__checkSer():
            self.serialCon.write(msg.encode('utf-8'))
        else:
            print("Could not write to Serial")

    def __checkSer(self):
        if self.serialCon.is_open:
            return 1
        else:
            print("Connection lost")
            return 0

    def pixelOn(self, positions):
        for pixel in positions:
            if pixel not in self.mypixels:
                self.mypixels.append(pixel)
                self.__writeSer('1x{}x{}{};'.format(pixel[0], pixel[1], hex(pixel[3])[2:]))

    def pixelOff(self, positions):
        # --> einspeichern nochmal überlegen bzw. rauslöschen
        for pixel in positions:
            if pixel in self.mypixels:
                self.__writeSer('0x{}x{}x000000;'.format(pixel[0], pixel[1]))
                self.mypixels.remove(pixel)


if __name__ == '__main__':
    disp = Display('COM3', 19200)
    disp.pixelOn([[1, 2, 1, 16777215], [3, 1, 1, 16777215], [4, 1, 1, 16777215]])
    disp.pixelOff([[1, 2, 1]])
    sleep(10)
