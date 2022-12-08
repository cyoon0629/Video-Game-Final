class Settings:

    def __init__(self):
        #initialize game settings

        self.screen_width = 1000
        self.screen_height = 600
        self.bg_color = (230,230,230)

        #ship settings
        self.jetman_uspeed = 3
        self.jetman_dspeed = 1.5
        self.jetman_limit = 2

        #bullet settings
        self.bullet_speed = 1.5
        self.bullet_width = 30
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 3

        #alien settings
        self.wall_speed = 1
        self.fleet_drop_speed = 10
        #fleet_direction of 1 is right, -1 is left
        self.fleet_direction = 1
