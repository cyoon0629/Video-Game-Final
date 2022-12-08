import pygame
from pygame.sprite import Sprite

class bullets(Sprite):

    def __init__(self, ai_game):
        #create bullet object at ship's current position
        super().__init__()
        self.screen = ai_game.screen
        self.fsettings = ai_game.fsettings
        self.color = self.fsettings.bullet_color

        #create bullet rect at (0,0) then set correct position
        self.rect = pygame.Rect(0,0, self.fsettings.bullet_width, self.fsettings.bullet_height)
        self.rect.midtop = ai_game.jetman.rect.midtop

        #store bullet's position as decimal
        self.x = float(self.rect.x)

    def update(self):
        #move bullet up screen
        self.x += self.fsettings.bullet_speed

        #update rect position
        self.rect.x = self.x

    def draw_bullet(self):
        pygame.draw.rect(self.screen,self.color,self.rect)

