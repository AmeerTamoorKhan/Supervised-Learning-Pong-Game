class Player:
    def __init__(self, screen, width, player, x, y, v):
        self.screen = screen
        self.width = width
        self.player = player
        self.x = x
        self.y = y
        self.v = v

    def update(self):
        self.x = self.x + self.v
        # Check for the Collision
        self.collision()
        # Update the Position of the Paddle
        self.screen.blit(self.player, (self.x, self.y))
        return self.x, self.y

    def collision(self):
        if self.x < 0:
            self.x = self.x - self.v
        elif self.x > self.width - self.player.get_size()[0]:
            self.x = self.x - self.v
