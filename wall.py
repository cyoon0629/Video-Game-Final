import pygame
from pygame.sprite import Sprite

class Wall(Sprite):
    def __init__(self, ai_game):
        #initialize alien and starting position
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.fsettings

        #load alien image and set its rect attribute
        self.image = pygame.image.load('images/ghost.png')
        self.rect = self.image.get_rect()

        #start each new alien at top left of screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #store alien's decimal horizontal position
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def check_edges(self):
        #return true if alien at edge of screen
        screen_rect = self.screen.get_rect()
        if self.rect.bottom >= screen_rect.bottom or self.rect.top <= 0:
            return True

    def update(self):
        #move alien right
        self.y += self.settings.wall_speed * self.settings.fleet_direction
        self.rect.y = self.y