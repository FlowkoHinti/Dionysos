import random
from Raspberry.Dionysos import Dionysos
from time import sleep
from multiprocessing import Process, Queue
import time

life = 0
# Speed of the Snake in seconds
speeds = [0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7]
snakespeed = speeds[life]

# Size of the display
maxX = 8
maxY = 8

# Adjustable colors (r,g,b,c,m,y,w)
snakecolor = ['g', 'b', 'r', 'y', 'm', 'c', 'w']
foodcolor = ['r', 'm', 'c', 'b', 'w', 'y', 'g']


class Snake:
    snakedir = None
    alive = True

    def __init__(self, display_width, display_hight, color, ticks, food_color):
        self.max_x = display_width - 1
        self.max_y = display_hight - 1

        self.snake = [[display_width // 2, display_hight // 2],  # Head
                      [display_width // 2 - 1, display_hight // 2],  # Middle
                      [display_width // 2 - 2, display_hight // 2]]  # Tail

        self.snake_color = color
        self.ticks = ticks
        self.food = None
        self.food_color = food_color

        self.Display = Dionysos

    def start_up(self):
        pass
        self.new_food()
        # for part in self.snake:
        # self.ledmatrix.ledon(part, self.snake_color)
        # self.ledmatrix.ledon(self.food, self.foodcolor)

        sleep(1)

    def get_head(self):
        return self.snake[0]

    def get_next_pos(self, direction):
        head = self.get_head()

        if direction is "w" and self.check_next_pos('w'):
            if head[1] == self.max_y:
                return [head[0], 0]
            else:
                return [head[0], head[1] + 1]

        elif direction is "s" and self.check_next_pos('s'):
            if head[1] == 0:
                return [head[0], self.max_y]
            else:
                return [head[0], head[1] - 1]

        elif direction is "d" and self.check_next_pos('d'):
            if head[0] == self.max_x:
                return [0, head[1]]
            else:
                return [head[0] + 1, head[1]]

        elif direction is "a" and self.check_next_pos('a'):
            if head[0] == 0:
                return [self.max_x, head[1]]
            else:
                return [head[0] - 1, head[1]]

    def move_in_direction(self, new):
        self.snake.insert(0, new)
        # eher in die move funktion?
        # self.ledmatrix.ledon([x, y], self.snake_color)
        # self.ledmatrix.ledoff(self.snake[-1], self.snake_color)
        self.snake.pop()

    def move_snake(self, direction):

        if direction is "w" and self.check_next_pos('w'):
            self.move_in_direction(self.get_next_pos('w'))

        elif direction is "s" and self.check_next_pos('s'):
            self.move_in_direction(self.get_next_pos('s'))

        elif direction is "d" and self.check_next_pos('d'):
            self.move_in_direction(self.get_next_pos('d'))

        elif direction is "a" and self.check_next_pos('a'):
            self.move_in_direction(self.get_next_pos('a'))

        sleep(self.ticks)

    def check_next_pos(self, direction):
        head = self.get_head()

        if direction is 'w':
            next_pos = [head[0], head[1] + 1]

            if next_pos in self.snake or next_pos[1] > self.max_y:
                self.death()
                return False
            elif next_pos == self.food:
                self.eat(self.food[0], self.food[1], next_pos)
                return False
            return True

        elif direction == 's':
            next_pos = [head[0], head[1] - 1]

            if next_pos in self.snake or next_pos[1] < 1:
                self.death()
                return False
            elif next_pos == self.food:
                self.eat(self.food[0], self.food[1], next_pos)
                return False

            return True
        elif direction == 'd':
            next_pos = [head[0] + 1, head[1]]

            if next_pos in self.snake or next_pos[0] > self.max_x:
                self.death()
                return False
            elif next_pos == self.food:
                self.eat(self.food[0], self.food[1], next_pos)
                return False
            return True

        elif direction == 'a':
            next_pos = [head[0] - 1, head[1]]

            if next_pos in self.snake or next_pos[0] < 1:
                self.death()
                return False
            elif next_pos == self.food:
                self.eat(self.food[0], self.food[1], next_pos)
                return False
            return True

    @staticmethod
    def border_reached(next_pos):
        pass

    def eat(self):

        # self.ledmatrix.ledoff(self.food, self.foodcolor)
        self.food = self.new_food()
        # self.ledmatrix.ledon(self.food, self.foodcolor)

        self.snake.insert(0, next_pos)
        # self.ledmatrix.ledon(next_pos, self.snakecolor)
        self.snake_length += 1
        return True

    def new_food(self):
        rand_x = random.randint(1, self.max_x)
        rand_y = random.randint(1, self.max_y)
        if [rand_x, rand_y] == self.food or [rand_x, rand_y] in self.snake:
            self.new_food()
        self.food = [rand_x, rand_y]

    def death(self):
        self.alive = False
        head = self.get_head()
        for i in range(7):
            # self.ledmatrix.ledon(head, self.snakecolor)
            sleep(0.2)
            # self.ledmatrix.ledoff(head, self.snakecolor)
            sleep(0.2)

        # self.ledmatrix.matrixclear()
        # print("Score = " + str(self.snakelength))
        return False

    def win(self):
        # self.ledmatrix.matrixclear()
        self.alive = False

    @staticmethod
    def is_opposite_dir(dir):
        if dir is None:
            return 'a'
        elif dir == 'w':
            return 's'
        elif dir == 's':
            return 'w'
        elif dir == 'd':
            return 'a'
        elif dir == 'a':
            return 'd'


if __name__ == '__main__':
    """ÜBERARBEITEN"""
    """

    while 1:
        while life < 7:
            snake = Snake(maxX, maxY, snakecolor[life], snakespeed, foodcolor[life])
            q = Queue(1)
            process = Process(target=readdirection, args=(q,))
            process.deamon = True
            process.start()

            while snake.alive:
                if snake.snake_length == (maxX * maxY) - 1:
                    snake.win()
                    life = 6
                else:
                    if not q.empty():
                        try:
                            if not q.get() == is_opposite_dir(snake.snakedir):
                                snake.snakedir = q.get(timeout=0.03)
                            elif snake.snake_length == 1:
                                snake.snakedir = q.get(timeout=0.03)
                        except:
                            #print("Empty Queue Exception")
                            continue
                    snake.move(snake.snakedir)
            process.terminate()
            life += 1
        life = 0
            """
