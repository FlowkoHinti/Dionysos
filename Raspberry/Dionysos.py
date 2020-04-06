# Elternklasse für die Spiele
from Raspberry import Display, Menu, Snake, Tetris
from pynput import keyboard
import subprocess


class Dionysos:
    screen = []  # --> all pixels x/y/c
    __screen_old = []  # --> for changes
    __del_pos = []  # --> to delete

    def __init__(self):
        self.__display = Display.Display('COM3', 19200)

    @staticmethod
    def __parse_format(pixel_vector):
        return [pixel_vector[0][0], pixel_vector[1][0], pixel_vector[3][0]]

    def add_pixel(self, pixel_vector):
        # --> other format than vector?
        if self.__check_pixel(pixel_vector):
            pixel = self.__parse_format(pixel_vector)
            self.screen.append(pixel)

    def del_pixel(self, pixel_vector):
        # --> other format than vector?
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

    def close_Ser(self):
        self.__display.serialCon.close()

    def draw_letter(self, letter, start_x, start_y):
        pass


class Input:
    __key = ''
    __allowed = []
    __listener = None

    def get_key(self):
        return self.__key

    def __on_press(self, key):
        try:
            if key.char in self.__allowed:
                self.__key = key.char.upper()
                print('alphanumeric key {0} pressed'.format(key))

        except AttributeError:
            if key == keyboard.Key.up:
                self.__on_press(keyboard.KeyCode.from_char('w'))
            elif key == keyboard.Key.down:
                self.__on_press(keyboard.KeyCode.from_char('s'))
            elif key == keyboard.Key.left:
                self.__on_press(keyboard.KeyCode.from_char('d'))
            elif key == keyboard.Key.right:
                self.__on_press(keyboard.KeyCode.from_char('a'))
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


def tetris():
    #ausführen, warten bis fertig
    pass


if __name__ == '__main__':
    dy = Dionysos()

    subprocess.run()
    # i = Input()
    # i.listener_start()
    # i.allowed_keys(['w'])

    # i.allowed_keys(['e', 'a', 'w', 's', 'd', '#']) #up/down/right/left arrows = w/s/d/a

    # men = Menu.Menu(dy)
    # men.start()

    # vector = numpy.array([[4], [2], [1], [9]])

    # vector1 = numpy.array([[2], [3], [1], [2672800]])

    # vector2 = numpy.array([[19], [3], [1], [167200]])

    # vector3 = numpy.array([[2], [3], [1], [167200]])

    # dy.add_pixel(vector)
    # dy.add_pixel(vector1)
    # dy.add_pixel(vector2)
    # dy.add_pixel(vector3)
    dy.print_pixels()

    #i.stop_listener()
