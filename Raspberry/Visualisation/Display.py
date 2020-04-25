import serial
import threading
from time import sleep


class Display:
    display_width = None
    display_height = None

    def __init__(self, port, baudrate):
        try:
            self.serialCon = serial.Serial(port, baudrate)
            # sleep(1)  # reset wenn Serial geöffnet wird
        except Exception:
            print("Couldn't open Serial port")
        self.__get_display()
        # self.__read_lines()

    def close_serial(self):
        self.serialCon.close()

    # def __read_lines(self):
    #     readThread = threading.Thread(target=self.__read_ser)
    #     readThread.start()

    def __read_ser(self):
        while True:
            print(self.serialCon.readline())

    def __get_display(self):
        while self.__check_ser():
            self.__write_ser('ACK')
            if b'SOGENUGACK' in self.serialCon.readline():
                self.display_width = int(self.serialCon.readline().decode('utf-8'))
                self.display_height = int(self.serialCon.readline().decode('utf-8'))
                break

    def __write_ser(self, msg):
        self.serialCon.write(msg.encode('utf-8'))

    def __check_ser(self):
        if self.serialCon.is_open:
            return True
        else:
            print("Connection lost")
            return False

    def screen_update_batch_tag(self):
        self.__write_ser('#')

    def pixel_on(self, pixel):
        self.__write_ser('[{},{},{}]'.format(pixel[0], pixel[1], pixel[2]))

    def pixel_off(self, pixel):
        self.__write_ser('[{},{},0]'.format(pixel[0], pixel[1]))
