import numpy
import time
from Raspberry.Dionysos import Dionysos as Display
from Raspberry.Dionysos import Input


class Tetris:
    Display = Display()
    Input = Input()
    Input.allowed_keys(["w", "a", "s", "d"])

    def __init__(self):
        self.pixel = [numpy.array([[-1], [-1], [-1], [-1]])]
        self.display_height = Tetris.Display.get_height()
        self.display_width = Tetris.Display.get_width()
        self.Input.listener_start()

    def remove_row(self):
        for test in range(self.display_height):
            count = 0
            for pixels in self.pixel:
                if pixels[1] == test:
                    count += 1
                if count == self.display_width:

                    items_to_remove = []
                    for pixels2 in self.pixel:
                        if pixels2[1] == test:
                            items_to_remove.append(pixels2)
                    # items_to_remove.sort()
                    for item in items_to_remove:
                        self.remove_array_from_list(item)
                        Tetris.Display.del_pixel(item)
                        time.sleep(0.1)
                        Tetris.Display.print_pixels()

                    # time.sleep(0.1)

                    for number in range(len(self.pixel)):
                        if int(self.pixel[number][1]) > test:
                            self.pixel[number] = numpy.subtract(self.pixel[number], numpy.array([[0], [1], [0], [0]]))

                    Tetris.Display.clear_screen()

                    for pixels2 in self.pixel:
                        Tetris.Display.add_pixel(pixels2)

                    Tetris.Display.print_pixels()

    def check_collision(self, pixel):
        if not 0 <= pixel[0] < self.display_width or not 0 <= pixel[1]:
            return True

        if not 0 <= pixel[1]:
            return True

        if self.pixel:
            for pixels in self.pixel:
                if pixel[0] == pixels[0] and pixel[1] == pixels[1]:
                    return True
            return False

    def remove_array_from_list(self, arr):
        ind = 0
        size = len(self.pixel)
        while ind != size and not numpy.array_equal(self.pixel[ind], arr):
            ind += 1
        if ind != size:
            self.pixel.pop(ind)
        else:
            raise ValueError('array not found in list.')


class Tetromino:
    __pieces = ["I", "O", "T", "S", "Z", "J", "L"]

    def __init__(self, tetris: Tetris):
        self.piece = numpy.random.choice(self.__pieces, 1)
        self.position = self.starting_position(self.piece, tetris.display_height, tetris.display_width)

        self.valid = True
        for pos in self.position:
            if tetris.check_collision(pos):
                self.valid = False

        if self.valid:
            for vector in self.position:
                Tetris.Display.add_pixel(vector)
            Tetris.Display.print_pixels()

    @staticmethod
    def starting_position(piece_symbol, display_height, display_width):
        if piece_symbol == "I":
            return [numpy.array([[(display_width//2)+0], [display_height-2], [1], [255]]),
                    numpy.array([[(display_width//2)-1], [display_height-2], [1], [255]]),
                    numpy.array([[(display_width//2)+1], [display_height-2], [1], [255]]),
                    numpy.array([[(display_width//2)+2], [display_height-2], [1], [255]])]
        elif piece_symbol == "O":
            return [numpy.array([[(display_width//2)+0], [display_height-2], [1], [255]]),
                    numpy.array([[(display_width//2)+0], [display_height-1], [1], [255]]),
                    numpy.array([[(display_width//2)+1], [display_height-2], [1], [255]]),
                    numpy.array([[(display_width//2)+1], [display_height-1], [1], [255]])]
        elif piece_symbol == "T":
            return [numpy.array([[(display_width//2)+0], [display_height-2], [1], [255]]),
                    numpy.array([[(display_width//2)+0], [display_height-1], [1], [255]]),
                    numpy.array([[(display_width//2)-1], [display_height-2], [1], [255]]),
                    numpy.array([[(display_width//2)+1], [display_height-2], [1], [255]])]
        elif piece_symbol == "S":
            return [numpy.array([[(display_width//2)+0], [display_height-2], [1], [255]]),
                    numpy.array([[(display_width//2)-1], [display_height-2], [1], [255]]),
                    numpy.array([[(display_width//2)+0], [display_height-1], [1], [255]]),
                    numpy.array([[(display_width//2)+1], [display_height-1], [1], [255]])]
        elif piece_symbol == "Z":
            return [numpy.array([[(display_width//2)+0], [display_height-2], [1], [255]]),
                    numpy.array([[(display_width//2)-1], [display_height-1], [1], [255]]),
                    numpy.array([[(display_width//2)+0], [display_height-1], [1], [255]]),
                    numpy.array([[(display_width//2)+1], [display_height-2], [1], [255]])]
        elif piece_symbol == "J":
            return [numpy.array([[(display_width//2)+0], [display_height-2], [1], [255]]),
                    numpy.array([[(display_width//2)-1], [display_height-1], [1], [255]]),
                    numpy.array([[(display_width//2)-1], [display_height-2], [1], [255]]),
                    numpy.array([[(display_width//2)+1], [display_height-2], [1], [255]])]
        elif piece_symbol == "L":
            return [numpy.array([[(display_width//2)+0], [display_height-2], [1], [255]]),
                    numpy.array([[(display_width//2)-1], [display_height-2], [1], [255]]),
                    numpy.array([[(display_width//2)+1], [display_height-2], [1], [255]]),
                    numpy.array([[(display_width//2)+1], [display_height-1], [1], [255]])]

    def gravity(self, tetris: Tetris):
        for pos in range(len(self.position)):
            temp = numpy.subtract(self.position[pos], numpy.array([[0], [1], [0], [0]]))
            if tetris.check_collision(temp):
                for pixels in self.position:
                    pixels[3] = 16711680
                    tetris.pixel.append(pixels)
                    Tetris.Display.add_pixel(pixels)
                Tetris.Display.print_pixels()
                tetris.remove_row()
                return Tetromino(tetris)

        # deletes old pixel state
        for pos in self.position:
            Tetris.Display.del_pixel(pos)
        Tetris.Display.print_pixels()

        for pos in range(len(self.position)):
            self.position[pos] = numpy.subtract(self.position[pos], numpy.array([[0], [1], [0], [0]]))

        # shows new pixels
        for pos in self.position:
            Tetris.Display.add_pixel(pos)
        Tetris.Display.print_pixels()

        return self

    def rotate(self, tetris: Tetris):
        # It is pointless to rotate this piece
        if self.piece == "O":
            return False

        # for translating the pixels to 0/0 in the coordinate system
        # the first pixel of every Tetromino is the reference point for the rotation
        first_translation_matrix = numpy.array([[1, 0, -int(self.position[0][0]), 0],
                                                [0, 1, -int(self.position[0][1]), 0],
                                                [0, 0, 1, 0],
                                                [0, 0, 0, 1]])

        # for translating the pixels back to the point of origin in the coordinate system
        # the first pixel of every Tetromino is the reference point for the rotation
        second_translation_matrix = numpy.array([[1, 0, int(self.position[0][0]), 0],
                                                 [0, 1, int(self.position[0][1]), 0],
                                                 [0, 0, 1, 0],
                                                 [0, 0, 0, 1]])

        rotation_matrix = numpy.array([[0, 1, 0, 0],
                                       [-1, 0, 0, 0],
                                       [0, 0, 1, 0],
                                       [0, 0, 0, 1]])

        # checks if the new pixel is valid (not colliding with anything)
        for pos in self.position:
            temp = pos
            temp = first_translation_matrix.dot(temp)
            temp = rotation_matrix.dot(temp)
            temp = second_translation_matrix.dot(temp)
            if tetris.check_collision(temp):
                return False

        # deletes old pixel state
        for pos in self.position:
            Tetris.Display.del_pixel(pos)
        Tetris.Display.print_pixels()

        # rotates the pixel by first translating them to 0/0 in the coordinate system
        # then applies a rotation matrix and translates them back to the original position
        for pos in range(len(self.position)):
            self.position[pos] = first_translation_matrix.dot(self.position[pos])
            self.position[pos] = rotation_matrix.dot(self.position[pos])
            self.position[pos] = second_translation_matrix.dot(self.position[pos])

        # shows new pixels
        for pos in piece.position:
            Tetris.Display.add_pixel(pos)
        Tetris.Display.print_pixels()

    def move(self, key, tetris: Tetris):
        if key == "a":
            for pos in range(len(self.position)):
                temp = numpy.subtract(self.position[pos], numpy.array([[1], [0], [0], [0]]))
                if tetris.check_collision(temp):
                    return False

            # deletes old pixel state
            for pos in self.position:
                Tetris.Display.del_pixel(pos)
            Tetris.Display.print_pixels()

            for pos in range(len(self.position)):
                self.position[pos] = numpy.subtract(self.position[pos], numpy.array([[1], [0], [0], [0]]))

            # shows new pixels
            for pos in self.position:
                Tetris.Display.add_pixel(pos)
            Tetris.Display.print_pixels()

        if key == "d":
            for pos in range(len(self.position)):
                temp = numpy.subtract(self.position[pos], numpy.array([[-1], [0], [0], [0]]))
                if tetris.check_collision(temp):
                    return False

            for pos in self.position:
                Tetris.Display.del_pixel(pos)
            Tetris.Display.print_pixels()

            for pos in range(len(self.position)):
                self.position[pos] = numpy.subtract(self.position[pos], numpy.array([[-1], [0], [0], [0]]))

            for pos in self.position:
                Tetris.Display.add_pixel(pos)
            Tetris.Display.print_pixels()


if __name__ == '__main__':
    Tetris = Tetris()
    piece = Tetromino(Tetris)
    exit_flag = False

    timestamp = time.time()
    while not exit_flag:
        if Tetris.Input.get_key() == "w":
            piece.rotate(Tetris)
            Tetris.Input.reset_key()

        if Tetris.Input.get_key() == "a" or Tetris.Input.get_key() == "d":
            piece.move(Tetris.Input.get_key(), Tetris)
            Tetris.Input.reset_key()

        while Tetris.Input.get_key() == "s":
            piece = piece.gravity(Tetris)
            if not piece.valid:
                exit_flag = True
            Tetris.Input.reset_key()
            time.sleep(0.01)

        # if time.time() > timestamp + 1:
        #     piece = piece.gravity(Tetris)
        #     if not piece.valid:
        #         exit_flag = True
        #     timestamp = time.time()

    Tetris.Display.clear_screen()
    Tetris.Display.close_serial()
    Tetris.Input.stop_listener()
