from numpy import array
from Raspberry import Dionysos


class Menu:
    __cursor_pos = 0
    __games = ['tetris', 'snake']
    __selection = []  # ring around

    def __init__(self, Dionysos):
        self.dy = Dionysos

    def start(self):
        self.__draw_menu()

        pass

    def get_pos(self):
        return self.__cursor_pos

    def __draw_menu(self):
        Dionysos.Dionysos.clear_screen(self.dy)
        # Dionysos.Dionysos.add_pixel(self.dy, array([[0], [0], [1], [55000]]))
        #

    def move_cursor(self, direction):
        # change color of selection
        # --> draw circle around selector ?
        # --> color of selector
        if direction == 'w':
            self.cursor_pos -= 1
            if self.cursor_pos < 0:
                self.cursor_pos = len(self.games)
        elif direction == 's':
            self.cursor_pos += 1
            if self.cursor_pos > len(self.games):
                self.cursor_pos = 0

        # delete old selection positions
        # add new positions
        # print screen
