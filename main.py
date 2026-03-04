# 游戏主程序入口

from config import *
from historical_events_extended import HISTORICAL_EVENTS
from game_mechanics import GAME_MECHANICS

class MinguoSimulator:
    def __init__(self):
        self.year = START_YEAR
        self.stats = INITIAL_STATS.copy()
        
    def start_game(self):
        print("=" * 50)
        print("历史模拟器：民国 (1912-1949)")
        print("=" * 50)
        print(f"游戏开始：{self.year}年")
        print(f"初始国力：{self.stats}")
        
    def next_turn(self):
        self.year += 1
        # 触发历史事件
        # 玩家决策
        # 更新国力
        pass

if __name__ == "__main__":
    game = MinguoSimulator()
    game.start_game()
