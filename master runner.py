import sys
from time import sleep
import pygame

from fsettings import Settings
from fgame_stats import GameStats
from jetman import jetman
from jetgirl import jetgirl
from bullets import bullets
from wall import Wall

class jetjoy:

    def __init__(self):
        pygame.init()
        self.fsettings = Settings()
        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.fsettings.screen_width = self.screen.get_rect().width
        self.fsettings.screen_height = self.screen.get_rect().height

        pygame.display.set_caption("Jetpack Joyride")

        self.stats = GameStats(self)
        self.jetman = jetman(self)
        #create group of bullets that will have their positions updated
        self.bullets = pygame.sprite.Group()
        self.wall = pygame.sprite.Group()

        self._create_fleet()

    def run_game(self) :
        while True:
            self._check_events()
            if self.stats.game_active:
                self.jetman.update()
                self._update_bullets()
                self._update_wall()
            self._update_screen()

    def _check_events(self):
        #respond to key and mouse presses
        #accesses keydown and keyup methods as its helper methods so this method is cleaner
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        if event.key == pygame.K_q:
            sys.exit()

        elif event.key == pygame.K_UP:
            self.jetman.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.jetman.moving_down = True

        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_UP:
            self.jetman.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.jetman.moving_down = True

    #def update(dt):
            # global bird_y
            # global bird_y_speed
            # global pipe_1_x
            # global pipe_2_x
            # global pipe_1_space_y
            # global pipe_2_space_y
            # jetman_y_speed += 900*dt
    # jetman_y += jetman_y_speed*dt

    def _fire_bullet(self):
        #create new bullet and add to bullets group
        if len(self.bullets) < self.fsettings.bullets_allowed:
            new_bullet = bullets(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        #update position of bullets
        self.bullets.update()

        # get rid of bullets that have disappeared
        for bullet in self.bullets.copy():
            if bullet.rect.right >= self.fsettings.screen_width:
                self.bullets.remove(bullet)
        self._check_bullet_wall_collisions()
    def _check_bullet_wall_collisions(self):
        #check if bullet hit alien, if so, delete that bullet and alien
        collisions = pygame.sprite.groupcollide(self.bullets, self.wall, True, True)

        #checks if fleet has been destroyed then repopulates it
        if not self.wall:
            #destroy existing bullets and create new fleet
            self.bullets.empty()
            self._create_fleet()
    def _create_fleet(self):
        #make alien
        wall = Wall(self)
        wall_width, wall_height = wall.rect.size
        jetman_width = self.jetman.rect.width
        #available space in x is width of screen minus the blank margins on either edge which is the width of one alien
        available_space_x = (self.fsettings.screen_width - wall_width - jetman_width)
        #each alien has its own width plus the blank space to its right which is also the width of an alien
        #number of aliens that will fit in the width of the screen
        number_wall_x = available_space_x // (2*wall_width)

        #find number of rows of aliens that fit on screen
        #put space between ship and first row of aliens equal to height of 3 aliens
        available_space_y = self.fsettings.screen_height - (2*wall_height)
        number_rows = available_space_y // (2*wall_height)


        for wall_number in range(number_wall_x):
            for row_number in range(number_rows):
                self._create_wall(wall_number, row_number)

    def _create_wall(self, wall_number, row_number):
        #create row of aliens
        wall = Wall(self)
        wall_width, wall_height = wall.rect.size
        jetman_width = self.jetman.rect.width
        #x and y position of alien
        wall.x = self.fsettings.screen_width - 2*wall_width - 2*wall_width*wall_number
        wall.rect.x = wall.x
        wall.y = wall_height + 2*wall_height*row_number
        wall.rect.y = wall.y
        self.wall.add(wall)
    def _update_wall(self):
        #if fleet at edge, update positions of all aliens in the fleet
        self._check_fleet_edges()
        self.wall.update()

        if pygame.sprite.spritecollideany(self.jetman, self.wall):
            self._jetman_hit()

        #look for aliens hitting left of screen
        self._check_wall_leftside()

    def _jetman_hit(self):
        #respond to ship being hit by alien
        #decrement ships left
        if self.stats.jetman_remain > 0:
            self.stats.jetman_remain -= 1

            #get rid of remaining aliens and bullets
            self.wall.empty()
            self.bullets.empty()

            #create new fleet and center ship
            self._create_fleet()
            self.jetman.center_jetman()

            #pause
            sleep(.5)
        else:
            #self.stats.game_active = False
            sys.exit()
    def _check_wall_leftside(self):
        #check if any aliens have reached bottom of screen
        screen_rect = self.screen.get_rect()
        for wall in self.wall.sprites():
            if wall.rect.left <= 0:
                #treat this the same as if ship got hit
                self._jetman_hit()
                break

    def _check_fleet_edges(self):
        #respond if alien reaches edge
        for wall in self.wall.sprites():
            if wall.check_edges():
                self._change_fleet_direction()
                break
    def _change_fleet_direction(self):
        #drop entire fleet and change fleet's direction
        for wall in self.wall.sprites():
            wall.rect.x -= self.fsettings.fleet_drop_speed
        self.fsettings.fleet_direction *= -1
    def _update_screen(self):
        # redraw screen during each pass through the loop
        self.screen.fill(self.fsettings.bg_color)

        self.jetman.blitme()

        for bullets in self.bullets.sprites():
            bullets.draw_bullet()

        self.wall.draw(self.screen)
        # make most recently drawn screen visible
        pygame.display.flip()

if __name__=='__main__':
    #make a game instance from class AlienInvasion and run game
    ai = jetjoy()
    ai.run_game()

