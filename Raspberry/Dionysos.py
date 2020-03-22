# Elternklasse für die Spiele
from Raspberry import Display
from Raspberry import Game
import numpy


class Dionysos:

    def __init__(self):
        self.__display = Display.Display('COM3', 19200)
        self.screen = []  # --> all pixel vectors
        self.__screen_old = []
        self.__del_pos = []

    def add_pixel(self, pixel_vector):
        if 0 <= pixel_vector[0, 0] < self.__display.display_width and 0 <= pixel_vector[
            1, 0] < self.__display.display_hight:  # probleme
            if self.__check_pixel(pixel_vector):
                self.screen.append(pixel_vector)
        else:
            print("Out of Display-boundaries")

    def del_pixel(self, pixel_vector):
        if not self.__check_pixel(pixel_vector):
            self.screen.remove(pixel_vector)
            self.__del_pos.append(pixel_vector)

    def __check_pixel(self, pixel_vector):
        if pixel_vector not in self.screen:  # probleme
            return True
        else:
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

    vector = numpy.array([[4],
                          [2],
                          [1],
                          [9]])

    vector1 = numpy.array([[2],
                           [3],
                           [1],
                           [167200]])

    vector2 = numpy.array([[22],
                           [3],
                           [1],
                           [167200]])

    vector3 = numpy.array([[2],
                           [3],
                           [1],
                           [167200]])

    dy.add_pixel(vector)
    dy.add_pixel(vector1)
    dy.add_pixel(vector2)
    dy.add_pixel(vector3)

    dy.print_pixels()
