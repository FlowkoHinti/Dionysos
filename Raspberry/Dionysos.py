# Elternklasse für die Spiele
from Raspberry import Display
from Raspberry import Game
import numpy


class Dionysos:

    def __init__(self):
        self.__display = Display.Display('COM3', 19200)
        self.screen = []  # --> all pixels x/y/c
        self.__screen_old = []
        self.__del_pos = []

    @staticmethod
    def __parse_format(pixel_vector):
        return [pixel_vector[0][0], pixel_vector[1][0], pixel_vector[3][0]]

    def add_pixel(self, pixel_vector):
        if self.__check_pixel(pixel_vector):
            pixel = self.__parse_format(pixel_vector)
            self.screen.append(pixel)

    def del_pixel(self, pixel_vector):
        if not self.__check_pixel(pixel_vector):
            pixel = self.__parse_format(pixel_vector)
            self.screen.remove(pixel)
            self.__del_pos.append(pixel)

    def __check_pixel(self, pixel_vector):
        pixel = self.__parse_format(pixel_vector)
        if pixel not in self.screen and 0 <= pixel[0] < self.__display.display_width and \
                0 <= pixel[1] < self.__display.display_hight:
            return True
        else:
            print("Pixel already active or out of boundaries")
            return False

    def print_pixels(self):
        for delpos in self.__del_pos:
            self.__display.pixel_off(delpos)
        self.__del_pos.clear()

        for pixel in self.screen:
            if pixel not in self.__screen_old:
                self.__display.pixel_on(pixel)
        self.__screen_old = self.screen.copy()

    def clear_screen(self):
        for pixel in self.screen:
            self.del_pixel(pixel)
        self.print_pixels()


if __name__ == '__main__':
    dy = Dionysos()

    vector = numpy.array([[4], [2], [1], [9]])

    vector1 = numpy.array([[2], [3], [1], [167200]])

    vector2 = numpy.array([[22], [3], [1], [167200]])

    vector3 = numpy.array([[2], [3], [1], [167200]])

    dy.add_pixel(vector)
    dy.add_pixel(vector1)
    # dy.add_pixel(vector2)
    # dy.add_pixel(vector3)

    dy.print_pixels()

    # thread.start input
    # thread handed over while initializing objects to use the raw input


def input():
    pass
    # reads the keyboard/controller input
    # is started as a thread and returns keypressed
