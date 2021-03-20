class GameStats():
    """跟踪游戏的统计信息"""

    def __init__(self, ai_settings):
        """初始化统计信息"""
        self.ai_settings = ai_settings
        self.update_stats()

        # 游戏运行状态
        self.game_active = True

    def update_stats(self):
        """初始化在游戏运行期间可能变化的统计信息"""
        self.ship_left = self.ai_settings.ship_limit
