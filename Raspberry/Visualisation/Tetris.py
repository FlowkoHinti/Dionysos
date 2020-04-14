import numpy
import time


class Tetromino:

    def __init__(self, piece_symbol):
        self.piece = piece_symbol
        self.position = self.starting_position(self.piece)

    @staticmethod
    def starting_position(piece_symbol):
        if piece_symbol == "I":
            return [numpy.array([[1], [1], [1], [16776960]]),
                    numpy.array([[2], [1], [1], [16776960]]),
                    numpy.array([[3], [1], [1], [16776960]]),
                    numpy.array([[4], [1], [1], [16776960]])]
        elif piece_symbol == "O":
            return [numpy.array([[2], [0], [1], [16776960]]),
                    numpy.array([[2], [1], [1], [16776960]]),
                    numpy.array([[3], [0], [1], [16776960]]),
                    numpy.array([[3], [1], [1], [16776960]])]
        elif piece_symbol == "T":
            return [numpy.array([[2], [0], [1], [16776960]]),
                    numpy.array([[1], [1], [1], [16776960]]),
                    numpy.array([[2], [1], [1], [16776960]]),
                    numpy.array([[3], [1], [1], [16776960]])]
        elif piece_symbol == "S":
            return [numpy.array([[1], [1], [1], [16776960]]),
                    numpy.array([[2], [1], [1], [16776960]]),
                    numpy.array([[2], [0], [1], [16776960]]),
                    numpy.array([[3], [0], [1], [16776960]])]
        elif piece_symbol == "Z":
            return [numpy.array([[1], [0], [1], [16776960]]),
                    numpy.array([[2], [0], [1], [16776960]]),
                    numpy.array([[2], [1], [1], [16776960]]),
                    numpy.array([[3], [1], [1], [16776960]])]
        elif piece_symbol == "J":
            return [numpy.array([[1], [0], [1], [16776960]]),
                    numpy.array([[1], [1], [1], [16776960]]),
                    numpy.array([[2], [1], [1], [16776960]]),
                    numpy.array([[3], [1], [1], [16776960]])]
        elif piece_symbol == "L":
            return [numpy.array([[1], [1], [1], [16776960]]),
                    numpy.array([[2], [1], [1], [16776960]]),
                    numpy.array([[3], [1], [1], [16776960]]),
                    numpy.array([[3], [0], [1], [16776960]])]


def tetris_main():
    from Raspberry.Dionysos import Dionysos as Display

    collision = False
    pieces = ["I", "O", "T", "S", "Z", "J", "L"]
    tetris = Display()

    print("****** Tetris ******")
    # print(piece.position)

    test = 0

    while not collision:
        piece = Tetromino(numpy.random.choice(pieces, 1))
        for vector in piece.position:
            tetris.add_pixel(vector)

        tetris.print_pixels()
        # time.sleep(0.25)
        tetris.clear_screen()
        # time.sleep(0.25)

        # test += 1
        #
        # if test > 0:
        #     collision = True
