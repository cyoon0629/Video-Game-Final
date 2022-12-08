class GameStats:
    #track game statistics

    def __init__(self, ai_game):
        self.settings = ai_game.fsettings
        self.reset_stats()

        #start alien invasion in active state
        self.game_active = True

    def reset_stats(self):
        #initialize statistics that can change during the game
        self.jetman_remain = self.settings.jetman_limit
