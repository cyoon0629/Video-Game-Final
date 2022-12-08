import pygame
import time

class jetman:

    def __init__(self, ai_game):
        #initialize image and starting position
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.fsettings = ai_game.fsettings

        #load image and get its rectangular parameters as if it were a rectangle
        self.image = pygame.image.load('images/boybaby.png')
        self.rect = self.image.get_rect()

        #start each new image at bottom center
        self.rect.midleft = self.screen_rect.midleft

        #store decimal value for image's horizontal position
        self.y = float(self.rect.y)

        #movement flag
        self.moving_up = False
        self.moving_down = False

    def update(self):
        t0 = time.time()
        while True:
            t_elapsed = time.time()-t0
            self.rect.y = self.y + 4.9(t_elapsed)(t_elapsed)

            #self.y += self.fsettings.jetman_uspeed
            #self.rect.y = self.y

        #if self.moving_up and self.rect.top > 0:
            #self.y -= self.fsettings.jetman_uspeed
        #if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            #self.y += self.fsettings.jetman_dspeed

        #update rect object from self.x
        #self.rect.y = self.y

    def center_jetman(self):
        #center ship on screen
        self.rect.midleft = self.screen_rect.midleft
        self.x = float(self.rect.x)
    def blitme(self):
        #draw image at current location
        self.screen.blit(self.image, self.rect)