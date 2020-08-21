
import pygame as pg
import numpy as np
from PingPong import Player, Ball, Display
from PingPong import TrainingData as TD
#from PingPong import LearningModel as lm
import random as rnd
import sys
from sklearn.neural_network import MLPClassifier as nn

class TestingMode:
    def __init__(self):
        pg.init()


        # Set the screen Width and the Height
        self.Width = 600
        self.Height = 600
        self.background = pg.image.load('Images/background.jpg')

        # Initialize the Pygame display
        self.screen = pg.display.set_mode((self.Width, self.Height))

        # Define the parameters for the Paddle
        self.player_img = pg.image.load('Images/Player.png')
        self.pLayer_x = self.Width / 2
        self.player_y = self.Height / 1.3
        self.player_speed = 0

        # Define the parameters for the Ball
        self.ball_img = pg.image.load('images/ball.png')
        self.ball_x = self.Width / 3
        self.ball_y = self.Height / 2
        self.ball_speed_x, self.ball_speed_y = 20, 20

        # Make an object of the class Display and Initialize it
        self.display = Display.Display(self.screen, self.Width, self.Height)
        # Make an object of the class Paddle and Initialize it
        self.player = Player.Player(self.screen, self.Width, self.player_img, self.pLayer_x, self.player_y, self.player_speed)
        # Make an object of the class Ball and Initialize it
        self.ball = Ball.Ball(self.screen, self.Width, self.Height, self.ball_img, self.ball_x, self.ball_y, self.ball_speed_x, self.ball_speed_y)
    # Main Game Loop

    def testingMode(self, clf):
        Input = 1
        running = True
        while running:

            #self.screen.fill((100, 100, 100))
            for events in pg.event.get():
                if events.type == pg.QUIT:
                    sys.exit()
            if Input == -1:
                self.player.v = -20
            if Input == 1:
                self.player.v = 20
            if Input == 0:
                self.player.v = 0

            # Update the position of the Paddle
            player_x, player_y = self.player.update()
            # Update the position of the Ball
            ball_x, ball_y, x_dir, y_dir, score = self.ball.update(player_x, player_y)
            if score == -1:
                ball_x = (self.Width-self.ball_img.get_size()[0])*rnd.random()
                ball_y = self.Height/2*rnd.random()
                self.ball = Ball.Ball(self.screen, self.Width, self.Height, self.ball_img, ball_x, ball_y, self.ball_speed_x, self.ball_speed_y)
            # Update the Display
            self.display.score(score)

            pg.display.update()
            self.screen.blit(self.background, (0, 0))
            InputData = np.array([player_x, ball_x, ball_y, x_dir, y_dir])
            Input = clf.predict([InputData])
            print(Input)


