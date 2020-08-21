import pygame as pg
import random
class Ball:
    def __init__(self, screen, width, height, ball, x, y, x_v, y_v):
        self.screen = screen
        self.width = width
        self.height = height
        self.ball = ball
        self.x = x
        self.y = y
        self.x_v = x_v
        self.y_v = y_v

        self.dir_x = 2*random.randint(0, 1) -1
        self.dir_y = 2*random.randint(0, 1) -1
        self.score = 0


    def update(self, player_x, player_y):

        self.dir_x, self.dir_y = self.collision(player_x, player_y)
        self.x = self.x + self.dir_x * self.x_v
        self.y = self.y + self.dir_y * self.y_v

        self.screen.blit(pg.transform.rotate(self.ball, 45), (self.x, self.y))
        return self.x, self.y, self.dir_x, self.dir_y, self.score

    def collision(self, ply_x, ply_y):

        if self.x < 0 and self.y < 0:
            return -self.dir_x, -self.dir_y
        elif self.x < 0 and self.y > 0:
            return -self.dir_x, self.dir_y
        elif self.x > 0 and self.y < 0:
            return self.dir_x, -self.dir_y
        elif self.x > self.width - self.ball.get_size()[0] and self.y < 5:
            return -self.dir_x, -self.dir_y
        elif self.x > self.width - self.ball.get_size()[0]:
            return -self.dir_x, self.dir_y
        elif self.x < self.width - self.ball.get_size()[0] and self.y > ply_y + 15:
            if ply_x-self.ball.get_size()[0] <= self.x <= ply_x + 128:
                self.score = self.score + 1
                return self.dir_x, -self.dir_y
            else:
                self.score = -1
                return 0, 0
        else:
            return self.dir_x, self.dir_y





