import random
from Raspberry.Dionysos import Input
from Raspberry.Dionysos import Dionysos
from time import sleep
import numpy

"""TODO:
Win condition
levels
"""


class Snake:
    d = Dionysos()
    i = Input()
    i.allowed_keys(["w", "a", "s", "d"])

    def __init__(self, display_width, display_height, color, ticks, food_color):
        self.max_x = display_width - 1
        self.max_y = display_height - 1

        self.snake = [[display_width // 2, display_height // 2],  # Head
                      [display_width // 2 - 1, display_height // 2],  # Middle
                      [display_width // 2 - 2, display_height // 2]]  # Tail

        self.snake_color = color
        self.ticks = ticks
        self.food = None
        self.food_color = food_color
        self.next_pos = None
        self.snake_dir = None
        self.alive = True

    @staticmethod
    def change_format(pos, color):
        return numpy.array([[pos[0]], [pos[1]], [1], [color]])

    @staticmethod
    def opposite_dir(direction):
        if direction == 'w':
            return 's'
        elif direction == 's':
            return 'w'
        elif direction == 'd':
            return 'a'
        elif direction == 'a':
            return 'd'

    def start_game(self):

        self.i.listener_start()
        self.new_food()

        for part in self.snake:
            self.d.add_pixel(self.change_format(part, self.snake_color))
        self.d.print_pixels()

        while self.i.get_key() is None or self.i.get_key() == 'a':
            self.i.get_key()

        while self.alive:
            if self.i.get_key() != self.opposite_dir(self.snake_dir):
                self.snake_dir = self.i.get_key()

            self.move_snake()
            self.d.print_pixels()
            sleep(self.ticks)

    def get_head(self):
        return self.snake[0]

    def get_next_pos(self):
        head = self.get_head()

        if self.snake_dir == "w":
            if head[1] == self.max_y:
                self.next_pos = [head[0], 0]
            else:
                self.next_pos = [head[0], head[1] + 1]

        elif self.snake_dir == "s":
            if head[1] == 0:
                self.next_pos = [head[0], self.max_y]
            else:
                self.next_pos = [head[0], head[1] - 1]

        elif self.snake_dir == "d":
            if head[0] == self.max_x:
                self.next_pos = [0, head[1]]
            else:
                self.next_pos = [head[0] + 1, head[1]]

        elif self.snake_dir == "a":
            if head[0] == 0:
                self.next_pos = [self.max_x, head[1]]
            else:
                self.next_pos = [head[0] - 1, head[1]]

    def move_snake(self):
        self.get_next_pos()
        if self.check_next_pos():
            self.snake.insert(0, self.next_pos)
            self.d.add_pixel(self.change_format(self.next_pos, self.snake_color))
            self.d.del_pixel(self.change_format(self.snake[-1], self.snake_color))
            self.snake.pop()

    def check_next_pos(self):
        if self.next_pos in self.snake:
            self.death()
            return False
        elif self.next_pos == self.food:
            self.eat()
            return False
        return True

    def eat(self):
        self.new_food()
        self.snake.insert(0, self.next_pos)
        self.d.add_pixel(self.change_format(self.next_pos, self.snake_color))

    def new_food(self):
        rand_x = random.randint(0, self.max_x)
        rand_y = random.randint(0, self.max_y)
        if [rand_x, rand_y] in self.snake or [rand_x, rand_y] == self.food:
            self.new_food()
        else:
            if self.food is not None:
                self.d.del_pixel(self.change_format(self.food, self.food_color))
            self.food = [rand_x, rand_y]
            self.d.add_pixel(self.change_format(self.food, self.food_color))

    def death(self):
        self.alive = False
        head = self.get_head()
        for i in range(7):
            self.d.del_pixel(self.change_format(head, self.snake_color))
            sleep(0.2)
            self.d.print_pixels()
            self.d.add_pixel(self.change_format(head, self.snake_color))
            sleep(0.2)
            self.d.print_pixels()

        self.d.clear_screen()

    def win(self):
        """In Progress"""
        # self.ledmatrix.matrixclear()
        self.alive = False


if __name__ == '__main__':
    s = Snake(5, 10, 3000066, 0.5, 9830402)
    s.start_game()


