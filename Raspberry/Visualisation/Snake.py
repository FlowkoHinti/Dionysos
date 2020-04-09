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
        self.max_x = display_width
        self.max_y = display_hight

        self.start_x = display_width // 2
        self.start_y = display_hight // 2
        self.snake = [[self.start_x, self.start_y], [self.start_x - 1, self.start_y], [self.start_x - 2, self.start_y]]
        self.snake_length = len(self.snake)
        self.snake_color = color
        self.ticks = ticks
        self.foodX = (self.max_x - self.start_x) // 2 + self.start_x
        self.foodY = self.start_y
        self.food = [self.foodX, self.foodY]
        self.foodcolor = food_color

        self.Display = Dionysos

        for part in self.snake:
            self.ledmatrix.ledon(part, self.snake_color)
        self.ledmatrix.ledon(self.food, self.foodcolor)

    def startup(self):

        sleep(1)

    def move(self, dir):

        head = self.get_head()
        tail = self.get_tail()

        headX = head[0]
        headY = head[1]
        tailX = tail[0]
        tailY = tail[1]

        if dir is "t" and self.check_next_pos('t', headX, headY):
            self.set_head(headX, headY + 1)
            self.set_tail(tailX, tailY)

        elif dir is "b" and self.check_next_pos('b', headX, headY):
            self.set_head(headX, headY - 1)
            self.set_tail(tailX, tailY)

        elif dir is "r" and self.check_next_pos('r', headX, headY):
            self.set_head(headX + 1, headY)
            self.set_tail(tailX, tailY)

        elif dir is "l" and self.check_next_pos('l', headX, headY):
            self.set_head(headX - 1, headY)
            self.set_tail(tailX, tailY)

        sleep(snakespeed)

    def get_head(self):
        snakehead = self.snake[0]
        return snakehead

    def get_tail(self):
        if self.snake_length < 2:
            snaketail = self.snake[-1]
        else:
            snaketail = self.snake[self.snake_length - 2]
        return snaketail

    def set_head(self, x, y):
        self.snake.insert(0, [x, y])
        # self.ledmatrix.ledon([x, y], self.snake_color)
        # self.ledmatrix.ledoff(self.snake[-1], self.snake_color)
        self.snake.pop()

    def set_tail(self, x, y):
        """ÜBERARBEITEN"""
        if self.snake_length < 2:
            return True
        self.snake[-1] = [x, y]

    def check_next_pos(self, dir, head_x, head_y):

        if dir is 't':
            next_pos = [head_x, head_y + 1]

            if next_pos in self.snake or next_pos[1] > self.max_y:
                self.death()
                return False
            elif next_pos == self.food:
                self.eat(self.food[0], self.food[1], next_pos)
                return False
            return True

        elif dir == 'b':
            next_pos = [head_x, head_y - 1]

            if next_pos in self.snake or next_pos[1] < 1:
                self.death()
                return False
            elif next_pos == self.food:
                self.eat(self.food[0], self.food[1], next_pos)
                return False

            return True
        elif dir == 'r':
            next_pos = [head_x + 1, head_y]

            if next_pos in self.snake or next_pos[0] > self.max_x:
                self.death()
                return False
            elif next_pos == self.food:
                self.eat(self.food[0], self.food[1], next_pos)
                return False
            return True

        elif dir == 'l':
            next_pos = [head_x - 1, head_y]

            if next_pos in self.snake or next_pos[0] < 1:
                self.death()
                return False
            elif next_pos == self.food:
                self.eat(self.food[0], self.food[1], next_pos)
                return False
            return True

    def eat(self, food_x, food_y, next_pos):
        randX = random.randint(1, self.max_x)
        randY = random.randint(1, self.max_y)
        new_food = [randX, randY]
        # print("new food location :" + str(randX) + ", " + str(randY))

        if new_food in self.snake or new_food == self.food:
            self.eat(food_x, food_y, next_pos)
        else:
            # self.ledmatrix.ledoff(self.food, self.foodcolor)
            self.food = new_food
            # self.ledmatrix.ledon(self.food, self.foodcolor)

        self.snake.insert(0, next_pos)
        # self.ledmatrix.ledon(next_pos, self.snakecolor)
        self.snake_length += 1
        return True

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
