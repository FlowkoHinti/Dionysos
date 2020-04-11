import numpy
import time


class Tetromino:

    def __init__(self, piece_symbol):
        self.piece = piece_symbol  # self.assign_piece(piece_symbol)
        self.position = self.starting_position(self.piece)

    @staticmethod
    def starting_position(piece_symbol):
        if piece_symbol == "I":
            return [numpy.array([[1], [0], [1], [16776960]]),
                    numpy.array([[2], [0], [1], [16776960]]),
                    numpy.array([[3], [0], [1], [16776960]]),
                    numpy.array([[4], [0], [1], [16776960]])]
        elif piece_symbol == "O":
            return "O"
        elif piece_symbol == "T":
            return "T"
        elif piece_symbol == "S":
            return "S"
        elif piece_symbol == "Z":
            return "Z"
        elif piece_symbol == "J":
            return "J"
        elif piece_symbol == "L":
            return "L"


def tetris_main():
    # from Raspberry.Dionysos import Dionysos as Display

    collision = False
    pieces = ["I", "O", "T", "S", "Z", "J", "L"]
    tetris = Display()

    # piece = Tetromino(numpy.random.choice(pieces, 1))
    piece = Tetromino("I")

    print("****** Tetris ******")

    print(piece.position)

    for vector in piece.position:
        tetris.add_pixel(vector)

    tetris.print_pixels()

    # while not collision:
    #     time.sleep(1)
    #     pass
    #
    # tetris.clear_screen()


if __name__ == '__main__':
    tetris_main()
