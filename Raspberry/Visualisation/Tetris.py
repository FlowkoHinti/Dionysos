import numpy
from Raspberry.Dionysos import Dionysos as Display, Input

class Tetromino:

    def __init__(self, piece_number):
        self.piece = self.assign_piece(piece_number)

    # @staticmethod
    def assign_piece(self, piece_number):
        if piece_number == "I":
            return "I"
        elif piece_number == "O":
            return "O"
        elif piece_number == "T":
            return "T"
        elif piece_number == "S":
            return "S"
        elif piece_number == "Z":
            return "Z"
        elif piece_number == "J":
            return "J"
        elif piece_number == "L":
            return "L"

    def spawn_piece(self):
        pass


if __name__ == '__main__':
    pieces = ["I", "O", "T", "S", "Z", "J", "L"]
    tertis = Display()

    tertis.add_pixel(numpy.array([[int()], [0], [1], [16711680]]))

    print("****** Tetris ******")
    piece = Tetromino(numpy.random.choice(pieces, 1))
