# Elternklasse für die Spiele
from Raspberry import Display
from Raspberry import Game
import numpy
from pynput import keyboard


class Dionysos:
    __display = Display.Display('COM3', 19200)
    screen = []  # --> all pixels x/y/c
    __screen_old = []  # --> for changes
    __del_pos = []  # --> to delete

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


class Input:
    def __on_press(key):
        try:
            print('alphanumeric key {0} pressed'.format(
                key.char))
        except AttributeError:
            print('special key {0} pressed'.format(
                key))

    def __on_release(key):
        print('{0} released'.format(
            key))
        if key == keyboard.Key.esc:
            # Stop listener
            return False

    listener = keyboard.Listener(
        on_press=__on_press,
        on_release=__on_release)

    # Collect events until released
    def listener_start(self):

        # ...or, in a non-blocking fashion:
        self.listener.isDaemon()
        self.listener.start()

    def stop_listener(self):
        self.listener.stop()


if __name__ == '__main__':
    dy = Dionysos()
    i = Input()
    i.listener_start()
    vector = numpy.array([[4], [2], [1], [9]])

    vector1 = numpy.array([[2], [3], [1], [2672800]])

    vector2 = numpy.array([[19], [3], [1], [167200]])

    vector3 = numpy.array([[2], [3], [1], [167200]])

    dy.add_pixel(vector)
    dy.add_pixel(vector1)
    # dy.add_pixel(vector2)
    # dy.add_pixel(vector3)

    dy.print_pixels()