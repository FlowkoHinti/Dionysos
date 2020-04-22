import threading
import numpy
import time


class Tetris:
    from Raspberry.Dionysos import Dionysos as Display
    from Raspberry.Dionysos import Input
    Display = Display()
    Input = Input()

    def __init__(self):
        self.pixel = []
        self.Input.listener_start()
        self.Input.allowed_keys(["w", "a", "s", "d"])


class Tetromino:
    __pieces = ["I", "O", "T", "S", "Z", "J", "L"]

    def __init__(self, tetris: Tetris):
        self.piece = numpy.random.choice(self.__pieces, 1)
        self.display_height = Tetris.Display.get_height()
        self.display_width = Tetris.Display.get_width()
        self.position = self.starting_position(self.piece, self.display_height, self.display_width)

        valid = True
        for pos in self.position:
            if self.check_collision(pos, tetris):
                valid = False

        if valid:
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
            if self.check_collision(temp, tetris):
                for pixels in self.position:
                    pixels[3] = 16711680
                    tetris.pixel.append(pixels)
                    Tetris.Display.add_pixel(pixels)
                Tetris.Display.print_pixels()

                for test in range(self.display_height):
                    count = 0
                    for pixels in tetris.pixel:
                        if pixels[1] == test:
                            count += 1
                        if count == self.display_width:
                            print("row " + str(test) + " is full")

                            for pixels2 in tetris.pixel:
                                if pixels2[1] == test:
                                    # tetris.pixel.remove(pixels2)
                                    Tetris.Display.del_pixel(pixels2)
                            Tetris.Display.print_pixels()

                            time.sleep(.5)

                            for number in range(len(tetris.pixel)):
                                if not self.check_collision(tetris.pixel[number], tetris):
                                    tetris.pixel[number] = numpy.subtract(tetris.pixel[number], numpy.array([[0], [1], [0], [0]]))

                            temp = tetris.pixel
                            tetris.pixel = []

                            for pixels2 in temp:
                                Tetris.Display.add_pixel(pixels2)
                                tetris.pixel.append(pixels2)
                            Tetris.Display.print_pixels()

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
            if self.check_collision(temp, tetris):
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
                if self.check_collision(temp, tetris):
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
                if self.check_collision(temp, tetris):
                    return False

            for pos in self.position:
                Tetris.Display.del_pixel(pos)
            Tetris.Display.print_pixels()

            for pos in range(len(self.position)):
                self.position[pos] = numpy.subtract(self.position[pos], numpy.array([[-1], [0], [0], [0]]))

            for pos in self.position:
                Tetris.Display.add_pixel(pos)
            Tetris.Display.print_pixels()

    def check_collision(self, pixel, tetris):
        if not 0 <= pixel[0] < self.display_width or not 0 <= pixel[1]:
            return True

        if not 0 <= pixel[1]:
            return True

        if tetris.pixel:
            for pixels in tetris.pixel:
                if pixel[0] == pixels[0] and pixel[1] == pixels[1]:
                    return True
            return False

    def delete_row(self, row, tetris):
        pass


if __name__ == '__main__':
    Tetris = Tetris()
    piece = Tetromino(Tetris)
    time.sleep(.5)

    while True:
        if Tetris.Input.get_key() == "w":
            piece.rotate(Tetris)
            Tetris.Input.reset_key()

        if Tetris.Input.get_key() == "a" or Tetris.Input.get_key() == "d":
            piece.move(Tetris.Input.get_key(), Tetris)
            Tetris.Input.reset_key()

        while Tetris.Input.get_key() == "s":
            piece = piece.gravity(Tetris)
            Tetris.Input.reset_key()
            time.sleep(0.01)

        # piece = piece.gravity(Tetris)
        # time.sleep(0.5)
