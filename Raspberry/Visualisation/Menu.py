from numpy import array


# from Raspberry import Dionysos as Game


class Menu:
    __cursor_pos = 0
    __games = ['tetris', 'snake']
    __selection = []  # ring around
    input = None

    def __init__(self, dionysos):
        self.dy = dionysos

    def start(self):
        self.__draw_menu()
        print("Menü gezeichnet")
        self.input = Game.Input()
        self.input.allowed_keys(["w", "s", "#"])
        self.input.listener_start()

        while self.input.get_key() != "#":
            self.move_cursor(self.input.get_key())

        self.input.stop_listener()

    def get_pos(self):
        return self.__cursor_pos

    def __draw_menu(self):
        Game.Dionysos.clear_screen(self.dy)
        print("Menü wird gezeichnet")

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
