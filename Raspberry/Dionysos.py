# Elternklasse für die Spiele
from Raspberry.Visualisation.Display import Display
# from Raspberry.Visualisation.Menu import Menu
# from Raspberry.Visualisation.Snake import Snake
# from Raspberry.Visualisation import Tetris
from pynput import keyboard
import subprocess
import numpy
import time


class Dionysos:
    screen = []  # --> all pixels x/y/c
    __screen_old = []  # --> for changes
    __del_pos = []  # --> to delete

    def __init__(self):
        self.__display = Display('COM3', 9600)

    @staticmethod
    def __parse_format(pixel_vector):
        return [pixel_vector[0][0], pixel_vector[1][0], pixel_vector[3][0]]

    def add_pixel(self, pixel_vector):
        # --> other format than vector?
        if self.__check_pixel(pixel_vector):
            self.screen.append(self.__parse_format(pixel_vector))

    def del_pixel(self, pixel_vector):
        # --> other format than vector?
        if not self.__check_pixel(pixel_vector):
            self.screen.remove(self.__parse_format(pixel_vector))
            self.__del_pos.append(self.__parse_format(pixel_vector))

    def __check_pixel(self, pixel_vector):
        pixel = self.__parse_format(pixel_vector)
        if pixel not in self.screen and 0 <= pixel[0] < self.__display.display_width and \
                0 <= pixel[1] < self.__display.display_height:
            return True
        else:
            print("Pixel already active or out of boundaries")
            return False

    def print_pixels(self):
        self.__display.screen_update_batch_tag()

        for del_pos in self.__del_pos:
            self.__display.pixel_off(del_pos)
        self.__del_pos.clear()

        for pixel in self.screen:
            if pixel not in self.__screen_old:
                self.__display.pixel_on(pixel)
        self.__screen_old = self.screen.copy()

        self.__display.screen_update_batch_tag()

    def clear_screen(self):
        # vllt nur c an Arduino und screen löschen
        for pixel in self.screen:
            self.__del_pos.append(pixel)
        self.screen.clear()
        self.print_pixels()

    def close_serial(self):
        self.__display.serialCon.close()

    def draw_letter(self, letter, start_x, start_y):
        pass

    def test_screen(self):
        for i in range(5):
            for j in range(10):
                self.add_pixel(numpy.array([[i], [j], [1], [16777215]]))
        self.print_pixels()
        # time.sleep(5)
        # self.clear_screen()


class Input:
    __key = None
    __allowed = []
    __listener = None

    def get_key(self):
        return self.__key

    def __on_press(self, key):
        try:
            if key.char in self.__allowed:
                self.__key = key.char.lower()
                print('alphanumeric key {0} pressed'.format(key))

        except AttributeError:
            if key == keyboard.Key.up:
                self.__on_press(keyboard.KeyCode.from_char('w'))
            elif key == keyboard.Key.down:
                self.__on_press(keyboard.KeyCode.from_char('s'))
            elif key == keyboard.Key.left:
                self.__on_press(keyboard.KeyCode.from_char('a'))
            elif key == keyboard.Key.right:
                self.__on_press(keyboard.KeyCode.from_char('d'))
            elif key == keyboard.Key.enter:
                self.__on_press(keyboard.KeyCode.from_char('#'))  # ENTER = #
            #print('special key {0} pressed'.format(key))

    def __on_release(self, key):
        if key == keyboard.Key.esc:
            # Stop listener
            return False

    def allowed_keys(self, keys):
        # Adds all allowed keys for an illustration
        self.__allowed.clear()
        for key in keys:
            self.__allowed.append(key)

    def listener_start(self):
        try:
            self.__listener = keyboard.Listener(
                on_press=self.__on_press,
                on_release=self.__on_release)
            self.__listener.start()
        except Exception:
            print("Could not start listener")

    def stop_listener(self):
        self.__listener.stop()


def menu():
    # führt das Menü als Subprocess aus und wartet bis der Prozess fertig ist --> Möglichkeit Auswahl zurück zu pipen?
    pass
    test = subprocess.Popen

def snake():
    #auführen, warten bis fertig
    pass


if __name__ == '__main__':
    # tetris_main()

    # dy = Dionysos()
    # while True:
    #     dy.test_screen()
    #     dy.clear_screen()
    # i = Input()
    # i.listener_start()
    # i.allowed_keys(['w'])

    # i.allowed_keys(['e', 'a', 'w', 's', 'd', '#']) #up/down/right/left arrows = w/s/d/a

    # men = Menu.Menu(dy)
    # men.start()

    """vector = numpy.array([[0], [0], [1], [16711680]])
    vector1 = numpy.array([[1], [1], [1], [255]])
    vector2 = numpy.array([[2], [2], [1], [16711680]])
    vector3 = numpy.array([[3], [3], [1], [255]])
    vector4 = numpy.array([[4], [4], [1], [16711680]])

    vector5 = numpy.array([[3], [6], [1], [255]])
    vector6 = numpy.array([[2], [7], [1], [16711680]])
    vector7 = numpy.array([[1], [8], [1], [255]])
    vector8 = numpy.array([[0], [9], [1], [16711680]])

    vector9 = numpy.array([[4], [5], [1], [16711680]])
    vector10 = numpy.array([[4], [3], [1], [16711680]])

    dy.add_pixel(vector)
    dy.add_pixel(vector1)
    dy.add_pixel(vector2)
    dy.add_pixel(vector3)
    dy.add_pixel(vector4)
    dy.add_pixel(vector5)
    dy.add_pixel(vector6)
    dy.add_pixel(vector7)
    dy.add_pixel(vector8)
    dy.add_pixel(vector9)
    dy.add_pixel(vector10)
    dy.print_pixels()
    time.sleep(2)
    dy.clear_screen()"""
    # i.stop_listener()
