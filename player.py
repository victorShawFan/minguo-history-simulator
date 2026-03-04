# 玩家系统

class Player:
    def __init__(self, name):
        self.name = name
        self.decisions = []
        self.achievements = []
        
    def make_decision(self, event, choice):
        self.decisions.append({
            'event': event,
            'choice': choice
        })
        
    def unlock_achievement(self, achievement):
        self.achievements.append(achievement)
# Round 24
# Round 25
# Round 26
# Round 27
# Round 28
