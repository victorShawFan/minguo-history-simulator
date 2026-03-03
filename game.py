# 历史模拟器：民国
import random

class Game:
    def __init__(self):
        self.player = {
            'name': '',
            'money': 1000,
            'influence': 100
        }

    def start(self):
        print('欢迎来到《历史模拟器：民国》')

if __name__ == '__main__':
    game = Game()
    game.start()
