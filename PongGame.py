import pygame as pg
import numpy as np
from PingPong import Player, Ball, Display
from PingPong import TrainingData as TD
import sys
from sklearn.neural_network import MLPClassifier as nn
import random as rnd
import pickle


def main(gameMode, model):
    pg.init()


    # Set the screen Width and the Height
    Width = 600
    Height = 600

    # Initialize the Pygame display
    screen = pg.display.set_mode((Width, Height))

    # Define the parameters for the Paddle
    player_img = pg.image.load('Images/Player.png')
    pLayer_x = Width / 2
    player_y = Height / 1.3
    player_speed = 0

    # Define the parameters for the Ball
    ball_img = pg.image.load('images/ball.png')
    ball_x = (Width-ball_img.get_size()[0])*rnd.random()
    ball_y = Height/2*rnd.random()
    ball_speed_x, ball_speed_y = 20, 20

    # Make an object of the class Display and Initialize it
    display = Display.Display(screen, Width, Height)
    # Make an object of the class Paddle and Initialize it
    player = Player.Player(screen, Width, player_img, pLayer_x, player_y, player_speed)
    # Make an object of the class Ball and Initialize it
    ball = Ball.Ball(screen, Width, Height, ball_img, ball_x, ball_y, ball_speed_x, ball_speed_y)
    # Main Game Loop


    csvData = []
    clickFlag = 1
    running = True
    Input = 1
    while running:
        screen.fill((100, 100, 100))

        for events in pg.event.get():
            if events.type == pg.QUIT:
                sys.exit()
            if gameMode == 1:
                if events.type == pg.KEYDOWN:
                    if events.key == pg.K_LEFT:
                        player.v = -20
                        clickFlag = -1
                    if events.key == pg.K_RIGHT:
                        player.v = 20
                        clickFlag = 1
                if events.type == pg.KEYUP:
                    if events.key == pg.K_RIGHT or events.key == pg.K_LEFT:
                        player.v = 0
                        clickFlag = 0

        if gameMode == 0:
            if Input == -1:
                player.v = -20
            elif Input == 1:
                player.v = 20
            elif Input == 0:
                player.v = 0



        # Update the position of the Paddle
        player_x, player_y = player.update()
        # Update the position of the Ball
        ball_x, ball_y, x_dir, y_dir, score = ball.update(player_x, player_y)
        if score == -1:
            ball_x = (Width-ball_img.get_size()[0])*rnd.random()
            ball_y = Height/2*rnd.random()
            ball = Ball.Ball(screen, Width, Height, ball_img, ball_x, ball_y, ball_speed_x, ball_speed_y)
        # Update the Display
        display.score(score)
        pg.display.update()
        #Input = model.predict([[player_x, ball_x, ball_y, x_dir, y_dir]])

        if gameMode == 1:
            csvData.append([player_x, ball_x, ball_y, x_dir, y_dir, clickFlag])

    if gameMode == 1:
        csvData = np.array(csvData)
        TD.write('Training Data.csv', ['x', 'y', 'click'], csvData)


if __name__ == '__main__':
    main(gameMode=1, model=0)
