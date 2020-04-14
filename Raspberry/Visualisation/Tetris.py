import numpy
import time
from Raspberry.Dionysos import Dionysos as Display


class Tetromino:

    def __init__(self, piece_symbol, display_height, display_width):
        self.piece = piece_symbol
        self.display_height = display_height
        self.display_width = display_width
        self.position = self.starting_position(self.piece, self.display_height, self.display_width)

    @staticmethod
    def starting_position(piece_symbol, display_height, display_width):
        if piece_symbol == "I":
            return [numpy.array([[(display_width//2)-1], [display_height-2], [1], [16776960]]),
                    numpy.array([[(display_width//2)+0], [display_height-2], [1], [16776960]]),
                    numpy.array([[(display_width//2)+1], [display_height-2], [1], [16776960]]),
                    numpy.array([[(display_width//2)+2], [display_height-2], [1], [16776960]])]
        elif piece_symbol == "O":
            return [numpy.array([[(display_width//2)+0], [display_height-2], [1], [16776960]]),
                    numpy.array([[(display_width//2)+0], [display_height-1], [1], [16776960]]),
                    numpy.array([[(display_width//2)+1], [display_height-2], [1], [16776960]]),
                    numpy.array([[(display_width//2)+1], [display_height-1], [1], [16776960]])]
        elif piece_symbol == "T":
            return [numpy.array([[(display_width//2)+0], [display_height-1], [1], [16776960]]),
                    numpy.array([[(display_width//2)-1], [display_height-2], [1], [16776960]]),
                    numpy.array([[(display_width//2)+0], [display_height-2], [1], [16776960]]),
                    numpy.array([[(display_width//2)+1], [display_height-2], [1], [16776960]])]
        elif piece_symbol == "S":
            return [numpy.array([[(display_width//2)-1], [display_height-2], [1], [16776960]]),
                    numpy.array([[(display_width//2)+0], [display_height-2], [1], [16776960]]),
                    numpy.array([[(display_width//2)+0], [display_height-1], [1], [16776960]]),
                    numpy.array([[(display_width//2)+1], [display_height-1], [1], [16776960]])]
        elif piece_symbol == "Z":
            return [numpy.array([[(display_width//2)-1], [display_height-1], [1], [16776960]]),
                    numpy.array([[(display_width//2)+0], [display_height-1], [1], [16776960]]),
                    numpy.array([[(display_width//2)+0], [display_height-2], [1], [16776960]]),
                    numpy.array([[(display_width//2)+1], [display_height-2], [1], [16776960]])]
        elif piece_symbol == "J":
            return [numpy.array([[(display_width//2)-1], [display_height-1], [1], [16776960]]),
                    numpy.array([[(display_width//2)-1], [display_height-2], [1], [16776960]]),
                    numpy.array([[(display_width//2)+0], [display_height-2], [1], [16776960]]),
                    numpy.array([[(display_width//2)+1], [display_height-2], [1], [16776960]])]
        elif piece_symbol == "L":
            return [numpy.array([[(display_width//2)-1], [display_height-2], [1], [16776960]]),
                    numpy.array([[(display_width//2)+0], [display_height-2], [1], [16776960]]),
                    numpy.array([[(display_width//2)+1], [display_height-2], [1], [16776960]]),
                    numpy.array([[(display_width//2)+1], [display_height-1], [1], [16776960]])]

    def gravity(self):
        for pos in range(len(self.position)):
            if not 0 < int(self.position[pos][1]) < self.display_height:
                return self
        for pos in range(len(self.position)):
            self.position[pos] = numpy.subtract(self.position[pos], numpy.array([[0], [1], [0], [0]]))


if __name__ == '__main__':
    pieces = ["I", "O", "T", "S", "Z", "J", "L"]
    tetris = Display()

    print("****** Tetris ******")
    while True:
        collision = 0
        piece = Tetromino(numpy.random.choice(pieces, 1), 10, 5)
        for vector in piece.position:
            tetris.add_pixel(vector)
        tetris.print_pixels()

        time.sleep(1)

        while collision < 11:
            piece.gravity()
            tetris.clear_screen()

            for vector in piece.position:
                tetris.add_pixel(vector)

            # time.sleep(0.25)
            tetris.print_pixels()
            time.sleep(0.25)
            collision += 1

        # piece = Tetromino(numpy.random.choice(pieces, 1), 10, 5)
        # # piece = Tetromino("O", 10, 5)
        # for vector in piece.position:
        #     tetris.add_pixel(vector)
        #
        # tetris.print_pixels()
        # time.sleep(0.2)
        # tetris.clear_screen()
        # time.sleep(0.2)
