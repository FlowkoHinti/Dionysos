from Raspberry import Dionysos


class Menu(Dionysos):
    cursor_pos = 0

    def __init__(self, input_handler, dionysos):
        self.input = input_handler
        self.display = dionysos
        pass

    def menu_init(self):
        self.display.clear_screen()

        pass

    def game_start(self):
        pass

    def move_cursor(self, direction):
        pass
