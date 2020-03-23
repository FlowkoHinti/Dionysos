import serial
import threading
import numpy
from time import sleep


class Display:
    display_width = 0
    display_hight = 0

    def __init__(self, port, baudrate):
        try:
            self.serialCon = serial.Serial(port, baudrate)
            sleep(2)  # reset wenn Serial geöffnet wird
        except:
            print("Couldn't open Serial port")
        self.__get_display()
        self.__read_lines()

    def __read_lines(self):
        readThread = threading.Thread(target=self.__read_ser)
        readThread.isDaemon()
        readThread.start()

    def __read_ser(self):
        while self.__check_ser():
            print(self.serialCon.readline())

    def __get_display(self):
        while self.__check_ser():
            self.__write_ser('ACK')
            if b'SOGENUGACK' in self.serialCon.readline():
                self.display_width = int(self.serialCon.readline().decode('utf-8'))
                self.display_hight = int(self.serialCon.readline().decode('utf-8'))
                break

    def __write_ser(self, msg):
        if self.__check_ser():
            self.serialCon.write(msg.encode('utf-8'))
        else:
            print("Could not write to Serial")

    def __check_ser(self):
        if self.serialCon.is_open:
            return True
        else:
            print("Connection lost")
            return False

    def pixel_on(self, pixel):
        self.__write_ser('{}x{}{};'.format(pixel[0], pixel[1], hex(pixel[2])[1:]))

    def pixel_off(self, pixel):
        self.__write_ser('{}x{}x0;'.format(pixel[0], pixel[1]))
