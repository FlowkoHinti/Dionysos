import serial
import threading
from queue import Queue
from time import sleep


class Display:

    def __init__(self, port, baudrate):
        try:
            self.serialCon = serial.Serial(port, baudrate)
        except:
            print("Couldn't open Serial port")

        self.displayWidth = 0
        self.displayHight = 0
        self.received = Queue()
        self.__getDisplay()
        self.__readLines()

    def __readLines(self):
        readThread = threading.Thread(target=self.__readSer)
        readThread.isDaemon()
        readThread.start()

    def __readSer(self):
        while self.__checkSer():
            try:
                self.received.put(self.serialCon.readline())
                print(self.received.get())
            except:
                print("Couldn't read Serial")

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

    def pixelOn(self, positions, hex):
        # Array von Positionen oder lieber komplettes 2D array? --> wäre vllt für die spiele einfacher muss man ja nur das komplette Array pushen
        # Absprache mit Dominik
        for pixel in positions:
            self.__writeSer('1x{}x{}x{};'.format(pixel[0], pixel[1], hex))

    def pixelOff(self):
        return 1


if __name__ == '__main__':
    disp = Display('COM3', 19200)
    disp.pixelOn([[1, 2], [3, 1], [4, 1]], 'FFFFFF')
    sleep(10)
