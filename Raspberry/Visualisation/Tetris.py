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
    from Raspberry.Dionysos import Dionysos as Display, Input

    collision = False
    pieces = ["I", "O", "T", "S", "Z", "J", "L"]
    tetris = Display()

    # piece = Tetromino("I")

    print("****** Tetris ******")
    # print(piece.position)

    # while not collision:
    piece = Tetromino(numpy.random.choice(pieces, 1))
    # for vector in piece.position:
    #     tetris.add_pixel(vector)

    tetris.add_pixel(numpy.array([[1], [0], [1], [16776960]]))
    tetris.add_pixel(numpy.array([[2], [0], [1], [16776960]]))
    tetris.add_pixel(numpy.array([[3], [0], [1], [16776960]]))
    tetris.add_pixel(numpy.array([[4], [0], [1], [16776960]]))
    tetris.add_pixel(numpy.array([[1], [1], [1], [16776960]]))
    tetris.add_pixel(numpy.array([[2], [1], [1], [16776960]]))
    tetris.add_pixel(numpy.array([[3], [1], [1], [16776960]]))
    tetris.add_pixel(numpy.array([[4], [1], [1], [16776960]]))
    # print(piece.piece)
    tetris.print_pixels()

    tetris.add_pixel(numpy.array([[1], [3], [1], [16776960]]))
    tetris.add_pixel(numpy.array([[2], [3], [1], [16776960]]))
    tetris.add_pixel(numpy.array([[3], [3], [1], [16776960]]))
    tetris.add_pixel(numpy.array([[4], [3], [1], [16776960]]))
    tetris.add_pixel(numpy.array([[1], [4], [1], [16776960]]))
    tetris.add_pixel(numpy.array([[2], [4], [1], [16776960]]))
    tetris.add_pixel(numpy.array([[3], [4], [1], [16776960]]))
    tetris.add_pixel(numpy.array([[4], [4], [1], [16776960]]))

    tetris.print_pixels()

    # time.sleep(0.25)
    # tetris.clear_screen()
    # time.sleep(2)

    # while not collision:
    #     time.sleep(1)
    #     pass
    #
    # tetris.clear_screen()
