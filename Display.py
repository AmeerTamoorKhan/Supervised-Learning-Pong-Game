import pygame as pg

class Display:
    def __init__(self, screen, width, height):
        self.screen = screen
        self.width = width
        self.height = height
        self.font = pg.font.Font('freesansbold.ttf', 24)

    def score(self, i):
        Score = self.font.render(f'Score: {i}', True, (255, 255, 255), (100, 100, 100))
        box = Score.get_rect()
        box.center = (65, 20)
        self.screen.blit(Score, box)

