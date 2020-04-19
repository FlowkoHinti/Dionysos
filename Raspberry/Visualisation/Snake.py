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
    display_width = d.get_width()
    display_height = d.get_height()

    def __init__(self, snake_color, ticks, food_color, level):
        self.max_x = self.display_width - 1
        self.max_y = self.display_height - 1

        self.snake = [[self.display_width // 2, self.display_height // 2],  # Head
                      [self.display_width // 2 - 1, self.display_height // 2],  # Middle
                      [self.display_width // 2 - 2, self.display_height // 2]]  # Tail

        self.snake_color = snake_color
        self.ticks = ticks
        self.food = None
        self.food_color = food_color
        self.next_pos = None
        self.snake_dir = None
        self.alive = False
        self.game_over = False
        self.score = 0
        self.total_score = self.score
        self.level = level

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

        while not self.game_over:
            self.new_food()

            for part in self.snake:
                self.d.add_pixel(self.change_format(part, self.snake_color))
            self.d.print_pixels()

            self.i.reset_key()
            while self.i.get_key() is None or self.i.get_key() == 'a':
                self.i.get_key()

            self.alive = True

            while self.alive:
                if self.i.get_key() != self.opposite_dir(self.snake_dir):
                    self.snake_dir = self.i.get_key()

                self.move_snake()
                self.d.print_pixels()
                sleep(self.ticks)
        self.i.stop_listener()
        self.d.clear_screen()
        self.d.close_serial()

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
        self.update_score()
        if (((self.display_width * self.display_height) - 3) * 100 * self.level) == self.score:
            self.win()

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
        self.game_over = True
        head = self.get_head()
        for i in range(7):
            self.d.del_pixel(self.change_format(head, self.snake_color))
            sleep(0.2)
            self.d.print_pixels()
            self.d.add_pixel(self.change_format(head, self.snake_color))
            sleep(0.2)
            self.d.print_pixels()

        self.d.clear_screen()

    def update_score(self):
        self.score += 100 * self.level

    def reset_snake(self):
        self.snake = [[self.display_width // 2, self.display_height // 2],  # Head
                      [self.display_width // 2 - 1, self.display_height // 2],  # Middle
                      [self.display_width // 2 - 2, self.display_height // 2]]  # Tail
        self.snake_dir = None
        self.next_pos = None
        self.food = None

    def win(self):
        self.alive = False
        self.level += 1
        self.total_score += self.score
        self.score = 0
        self.reset_snake()
        self.d.clear_screen()
        for x in range(self.max_x + 1):
            for y in range(self.max_y + 1):
                self.d.add_pixel(self.change_format([x, y], 16754688))
                self.d.print_pixels()
                sleep(0.1)
        sleep(1)
        self.d.clear_screen()


if __name__ == '__main__':
    s = Snake(65280, 0.5, 16711680, 1)
    s.start_game()


