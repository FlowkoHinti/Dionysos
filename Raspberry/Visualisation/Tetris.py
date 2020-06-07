import threading
import numpy
import time
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout


KV = '''
<MainLayout>
    orientation: "vertical"
    
    MDToolbar:
        title: "DIONYSOS"
        halign: "center"

    GridLayout:
        cols: 1
        spacing: 10, 10

        MDCard:
            size_hint: None, None
            size: "800dp", "480dp"

            BoxLayout:
                orientation: "vertical"
                spacing: 10

                TextInput:
                    id: my_textinput
                    halign: "center"
                    valign: "center"
                    size_hint: (1, 0.2)
                    text: "Next Piece:"
                    on_text: root.change_image()

                Image:
                    id: my_img
                    source: "C:/Users/Dominik/Desktop/Memes/8c52ec14be599270.jpg"
'''
# MDLabel:
#                     text: "Next Piece:"
#                     theme_text_color: "Primary"
#                     halign: "center"
#                     valign: "center"
#                     size_hint: (1, 0.2)
Builder.load_string(KV)


class MainLayout(BoxLayout):
    def change_image(self):
        my_img = self.ids['my_img']
        my_img.source = 'C:/Users/Dominik/Desktop/Memes/ableiten.jpg'


class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "LightBlue"
        self.main_layout = MainLayout()
        # test_thread = threading.Thread(target=tetris_main(self.main_layout))
        # test_thread.start()
        # self.img_change()
        return self.main_layout

        # layout = BoxLayout()
        # layout.add_widget(MainLayout)
        # layout.add_widget(Builder.load_string(KV))

    def img_change(self):
        self.main_layout.change_image()


class Tetris:
    from Raspberry.Dionysos import Dionysos as Display
    from Raspberry.Dionysos import Input
    Display = Display()
    Input = Input()
    Input.allowed_keys(["w", "a", "s", "d"])

    def get_active_pixels(self):
        return self.__active_pixels

    def set_active_pixels(self, pos):
        self.__active_pixels.append(pos)

    def get_display_height(self):
        return self.__display_height

    def get_display_width(self):
        return self.__display_width

    def get_speed(self):
        return self.__speed

    def increase_speed(self):
        self.__speed = numpy.power(2, self.__growth_coefficient * self.__block_count)

    def get_block_count(self):
        return self.__block_count

    def increase_block_count(self):
        self.__block_count += 1

    def __init__(self):
        self.Input.listener_start()
        self.__active_pixels = []
        self.__display_height = Tetris.Display.get_height()
        self.__display_width = Tetris.Display.get_width()
        self.__growth_coefficient = -(1 / (self.__display_width * self.__display_height // 2))
        self.__speed = 1
        self.__block_count = -1

    def check_rows(self):
        full_rows = []
        pixels_to_remove = []

        for row in range(self.__display_height):
            active_pixels = 0
            pixels_to_remove_temp = []

            for active_pixel in self.__active_pixels:
                if active_pixel[1] == row:
                    active_pixels += 1
                    pixels_to_remove_temp.append(active_pixel)
                if active_pixels == self.__display_width:
                    pixels_to_remove.extend(pixels_to_remove_temp)
                    full_rows.append(row)
                    break

        if full_rows:
            self.remove_rows(full_rows, pixels_to_remove)
            return True

        return False

    def remove_rows(self, rows, pixels_to_remove):
        for active_pixel in pixels_to_remove:
            self.remove_array_from_list(self.__active_pixels, active_pixel)
            Tetris.Display.del_pixel(active_pixel)
            Tetris.Display.print_pixels()
            time.sleep(0.05)

        for number, active_pixel in enumerate(self.__active_pixels):
            if int(active_pixel[1]) > rows[0]:
                Tetris.Display.del_pixel(active_pixel)
                self.__active_pixels[number] = numpy.subtract(active_pixel, numpy.array([[0], [len(rows)], [0], [0]]))
        Tetris.Display.print_pixels()

        for active_pixel in self.__active_pixels:
            if int(active_pixel[1]) >= rows[0]:
                Tetris.Display.add_pixel(active_pixel)
        Tetris.Display.print_pixels()

    def check_collision(self, pixel):
        if not 0 <= pixel[0] < self.__display_width or not 0 <= pixel[1]:
            return True

        if self.__active_pixels:
            for active_pixel in self.__active_pixels:
                if pixel[0] == active_pixel[0] and pixel[1] == active_pixel[1]:
                    return True
            return False
        return False

    @staticmethod
    def remove_array_from_list(lst, arr):
        ind = 0
        size = len(lst)
        while ind != size and not numpy.array_equal(lst[ind], arr):
            ind += 1
        if ind != size:
            lst.pop(ind)
        else:
            raise ValueError('array not found in list.')


class Tetromino:
    __pieces = ["I", "O", "T", "S", "Z", "J", "L"]

    def __init__(self, tetris: Tetris, new_piece=None):
        if not new_piece:
            self.piece = numpy.random.choice(self.__pieces, 1)
        else:
            self.piece = new_piece

        tetris.increase_block_count()
        tetris.increase_speed()

        self.__position = self.starting_position(self.piece, tetris.get_display_height(), tetris.get_display_width())
        self.__next_piece = numpy.random.choice(self.__pieces, 1)

        self.valid = True
        for pos in self.__position:
            if tetris.check_collision(pos):
                self.valid = False

        if self.valid:
            for vector in self.__position:
                tetris.Display.add_pixel(vector)
            tetris.Display.print_pixels()

    @staticmethod
    def starting_position(piece_symbol, display_height, display_width):
        if piece_symbol == "I":
            return [numpy.array([[(display_width//2)+0], [display_height-2], [1], [44991]]),
                    numpy.array([[(display_width//2)-1], [display_height-2], [1], [44991]]),
                    numpy.array([[(display_width//2)+1], [display_height-2], [1], [44991]]),
                    numpy.array([[(display_width//2)+2], [display_height-2], [1], [44991]])]
        elif piece_symbol == "O":
            return [numpy.array([[(display_width//2)+0], [display_height-2], [1], [12230656]]),
                    numpy.array([[(display_width//2)+0], [display_height-1], [1], [12230656]]),
                    numpy.array([[(display_width//2)+1], [display_height-2], [1], [12230656]]),
                    numpy.array([[(display_width//2)+1], [display_height-1], [1], [12230656]])]
        elif piece_symbol == "T":
            return [numpy.array([[(display_width//2)+0], [display_height-2], [1], [12517575]]),
                    numpy.array([[(display_width//2)+0], [display_height-1], [1], [12517575]]),
                    numpy.array([[(display_width//2)-1], [display_height-2], [1], [12517575]]),
                    numpy.array([[(display_width//2)+1], [display_height-2], [1], [12517575]])]
        elif piece_symbol == "S":
            return [numpy.array([[(display_width//2)+0], [display_height-2], [1], [98560]]),
                    numpy.array([[(display_width//2)-1], [display_height-2], [1], [98560]]),
                    numpy.array([[(display_width//2)+0], [display_height-1], [1], [98560]]),
                    numpy.array([[(display_width//2)+1], [display_height-1], [1], [98560]])]
        elif piece_symbol == "Z":
            return [numpy.array([[(display_width//2)+0], [display_height-2], [1], [13443073]]),
                    numpy.array([[(display_width//2)-1], [display_height-1], [1], [13443073]]),
                    numpy.array([[(display_width//2)+0], [display_height-1], [1], [13443073]]),
                    numpy.array([[(display_width//2)+1], [display_height-2], [1], [13443073]])]
        elif piece_symbol == "J":
            return [numpy.array([[(display_width//2)+0], [display_height-2], [1], [171]]),
                    numpy.array([[(display_width//2)-1], [display_height-1], [1], [171]]),
                    numpy.array([[(display_width//2)-1], [display_height-2], [1], [171]]),
                    numpy.array([[(display_width//2)+1], [display_height-2], [1], [171]])]
        elif piece_symbol == "L":
            return [numpy.array([[(display_width//2)+0], [display_height-2], [1], [16092696]]),
                    numpy.array([[(display_width//2)-1], [display_height-2], [1], [16092696]]),
                    numpy.array([[(display_width//2)+1], [display_height-2], [1], [16092696]]),
                    numpy.array([[(display_width//2)+1], [display_height-1], [1], [16092696]])]

    def gravity(self, tetris: Tetris):
        for pos in self.__position:
            temp = numpy.subtract(pos, numpy.array([[0], [1], [0], [0]]))

            if tetris.check_collision(temp):
                for pos2 in self.__position:
                    tetris.Display.del_pixel(pos2)
                    pos2[3] = 9342606
                    tetris.set_active_pixels(pos2)
                    tetris.Display.add_pixel(pos2)
                tetris.Display.print_pixels()
                tetris.check_rows()
                return Tetromino(tetris, self.__next_piece)

        # deletes old pixel state
        for pos in self.__position:
            tetris.Display.del_pixel(pos)
        tetris.Display.print_pixels()

        for pos in range(len(self.__position)):
            self.__position[pos] = numpy.subtract(self.__position[pos], numpy.array([[0], [1], [0], [0]]))

        # shows new pixels
        for pos in self.__position:
            tetris.Display.add_pixel(pos)
        tetris.Display.print_pixels()

        return self

    def rotate(self, tetris: Tetris):
        # It is pointless to rotate this piece
        if self.piece == "O":
            return True

        # for translating the pixels to 0/0 in the coordinate system
        # the first pixel of every Tetromino is the reference point for the rotation
        first_translation_matrix = numpy.array([[1, 0, -int(self.__position[0][0]), 0],
                                                [0, 1, -int(self.__position[0][1]), 0],
                                                [0, 0, 1, 0],
                                                [0, 0, 0, 1]])

        # for translating the pixels back to the point of origin in the coordinate system
        # the first pixel of every Tetromino is the reference point for the rotation
        second_translation_matrix = numpy.array([[1, 0, int(self.__position[0][0]), 0],
                                                 [0, 1, int(self.__position[0][1]), 0],
                                                 [0, 0, 1, 0],
                                                 [0, 0, 0, 1]])

        rotation_matrix = numpy.array([[-0, 1, 0, 0],
                                       [-1, 0, 0, 0],
                                       [-0, 0, 1, 0],
                                       [-0, 0, 0, 1]])

        # checks if the new pixel is valid (not colliding with anything)
        for pos in self.__position:
            temp = pos
            temp = first_translation_matrix.dot(temp)
            temp = rotation_matrix.dot(temp)
            temp = second_translation_matrix.dot(temp)
            if tetris.check_collision(temp):
                return False

        # deletes old pixel state
        for pos in self.__position:
            tetris.Display.del_pixel(pos)
        tetris.Display.print_pixels()

        # rotates the pixel by first translating them to 0/0 in the coordinate system
        # then applies a rotation matrix and translates them back to the original position
        for pos in range(len(self.__position)):
            self.__position[pos] = first_translation_matrix.dot(self.__position[pos])
            self.__position[pos] = rotation_matrix.dot(self.__position[pos])
            self.__position[pos] = second_translation_matrix.dot(self.__position[pos])

        # shows new pixels
        for pos in self.__position:
            tetris.Display.add_pixel(pos)
        tetris.Display.print_pixels()

    def move(self, key, tetris: Tetris):
        direction = 0

        if key == "a":
            direction = 1
        if key == "d":
            direction = -1

        for pos in self.__position:
            temp = numpy.subtract(pos, numpy.array([[direction], [0], [0], [0]]))
            if tetris.check_collision(temp):
                return False

        # deletes old pixel state
        for pos in self.__position:
            tetris.Display.del_pixel(pos)
        tetris.Display.print_pixels()

        for pos in range(len(self.__position)):
            self.__position[pos] = numpy.subtract(self.__position[pos], numpy.array([[direction], [0], [0], [0]]))

        # shows new pixels
        for pos in self.__position:
            tetris.Display.add_pixel(pos)
        tetris.Display.print_pixels()


def tetris_main():
    game = Tetris()
    piece = Tetromino(game)
    exit_flag = False
    timestamp = time.time()

    while not exit_flag:
        if game.Input.get_key() == "w":
            piece.rotate(game)
            game.Input.reset_key()

        if game.Input.get_key() == "a" or game.Input.get_key() == "d":
            piece.move(game.Input.get_key(), game)
            game.Input.reset_key()

        while game.Input.get_key() == "s":
            piece = piece.gravity(game)
            if not piece.valid:
                exit_flag = True
            game.Input.reset_key()
            timestamp = time.time()
            time.sleep(0.01)

        if time.time() > timestamp + game.get_speed():
            piece = piece.gravity(game)
            if not piece.valid:
                exit_flag = True
            timestamp = time.time()

    game.Display.clear_screen()
    game.Display.close_serial()
    game.Input.stop_listener()


if __name__ == '__main__':
    test_thread = threading.Thread(target=tetris_main)
    test_thread.start()
    MainApp().run()
    test_thread.join()
