class GameStats():
    """chase information """
    def __init__(self,ai_settings):
        """initial collecting infomation"""
        self.ai_settings = ai_settings
        self.reset_stats()
        # inactive game
        self.game_active = False
        #不重置最高分
        self.high_score = 0
        self.level = 1

    def reset_stats(self):
        """initial changing infomation"""
        self.ships_left =self.ai_settings.ship_limit
        self.score = 0

