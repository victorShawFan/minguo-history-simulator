# 历史模拟器：民国
"""
《历史模拟器：民国》- AI驱动的文字冒险策略游戏

灵感来源：
- Steam游戏：历史模拟器系列
- GLM-5驱动的《历史模拟器：崇祯》

技术架构：
- 使用GPT-5.1作为AI引擎驱动剧情和NPC对话
- 玩家扮演民国时期的历史人物
- 根据选择影响历史走向
"""

import random
import json
from datetime import datetime
from typing import Dict, List, Optional
from dataclasses import dataclass, field
from enum import Enum

class Era(Enum):
    EARLY_REPUBLIC = "北洋时期 (1912-1928)"
    NANJING_DECADE = "南京十年 (1928-1937)"
    SINO_JAPANESE_WAR = "抗日战争 (1937-1945)"
    CIVIL_WAR = "解放战争 (1945-1949)"

class Faction(Enum):
    BEIYANG = "北洋系"
    KMT = "国民党"
    CCP = "共产党"
    WARLORD = "军阀"
    MERCHANT = "商人"
    SCHOLAR = "学者"
    NONE = "无党派"

@dataclass
class Character:
    """角色类"""
    name: str
    title: str = ""
    faction: Faction = Faction.NONE
    money: int = 1000
    influence: int = 100
    military: int = 0
    intelligence: int = 50
    charisma: int = 50
    health: int = 100
    age: int = 25
    
    skills: List[str] = field(default_factory=list)
    relationships: Dict[str, int] = field(default_factory=dict)
    inventory: List[str] = field(default_factory=list)

@dataclass
class GameState:
    """游戏状态"""
    year: int = 1912
    month: int = 1
    era: Era = Era.EARLY_REPUBLIC
    current_location: str = "北京"
    current_event: str = ""
    history_log: List[str] = field(default_factory=list)
    turn: int = 0

class HistoricalEvent:
    """历史事件库"""
    
    EVENTS = {
        Era.EARLY_REPUBLIC: [
            {
                "name": "袁世凯称帝",
                "year": 1915,
                "description": "袁世凯宣布恢复帝制，建立中华帝国，年号洪宪。",
                "choices": [
                    {"text": "支持称帝", "effect": {"influence": -20, "money": 1000}},
                    {"text": "反对称帝", "effect": {"influence": 30, "military": 10}},
                    {"text": "保持中立", "effect": {"intelligence": 5}}
                ]
            },
            {
                "name": "护国运动",
                "year": 1916,
                "description": "蔡锷、唐继尧等发动护国战争，反对帝制。",
                "choices": [
                    {"text": "加入护国军", "effect": {"military": 20, "influence": 15}},
                    {"text": "支援物资", "effect": {"money": -500, "influence": 10}},
                    {"text": "观望局势", "effect": {}}
                ]
            },
            {
                "name": "五四运动",
                "year": 1919,
                "description": "北京学生发起反帝爱国运动，抗议巴黎和会将德国在山东权益转让日本。",
                "choices": [
                    {"text": "声援学生", "effect": {"influence": 25, "charisma": 10}},
                    {"text": "保持秩序", "effect": {"influence": -10, "money": 200}},
                    {"text": "撰文评论", "effect": {"intelligence": 10, "charisma": 5}}
                ]
            }
        ],
        Era.NANJING_DECADE: [
            {
                "name": "北伐战争",
                "year": 1928,
                "description": "国民革命军发动北伐，统一中国。",
                "choices": [
                    {"text": "参加北伐", "effect": {"military": 30, "influence": 20}},
                    {"text": "捐款支持", "effect": {"money": -1000, "influence": 15}},
                    {"text": "避居租界", "effect": {"health": 10}}
                ]
            },
            {
                "name": "九一八事变",
                "year": 1931,
                "description": "日本关东军发动事变，占领东北。",
                "choices": [
                    {"text": "呼吁抗日", "effect": {"influence": 20, "charisma": 15}},
                    {"text": "组织义勇军", "effect": {"military": 25, "health": -10}},
                    {"text": "南迁避难", "effect": {"money": -500}}
                ]
            }
        ],
        Era.SINO_JAPANESE_WAR: [
            {
                "name": "七七事变",
                "year": 1937,
                "description": "卢沟桥事变爆发，全面抗战开始。",
                "choices": [
                    {"text": "投笔从戎", "effect": {"military": 40, "health": -20}},
                    {"text": "后方支援", "effect": {"money": -2000, "influence": 30}},
                    {"text": "文化抗战", "effect": {"intelligence": 20, "charisma": 20}}
                ]
            }
        ]
    }

class MinguoGame:
    """民国历史模拟器主游戏类"""
    
    def __init__(self):
        self.player: Optional[Character] = None
        self.state = GameState()
        self.ai_client = None
        
    def initialize_ai(self, api_key: str = None):
        """初始化AI引擎（GPT-5.1）"""
        pass
    
    def create_character(self, name: str, background: str = "scholar") -> Character:
        """创建角色"""
        backgrounds = {
            "scholar": {"intelligence": 70, "charisma": 60, "faction": Faction.SCHOLAR},
            "merchant": {"money": 5000, "charisma": 50, "faction": Faction.MERCHANT},
            "military": {"military": 60, "health": 80, "faction": Faction.WARLORD},
            "revolutionary": {"influence": 50, "charisma": 70, "faction": Faction.KMT}
        }
        
        bg = backgrounds.get(background, backgrounds["scholar"])
        
        self.player = Character(
            name=name,
            intelligence=bg.get("intelligence", 50),
            charisma=bg.get("charisma", 50),
            money=bg.get("money", 1000),
            military=bg.get("military", 0),
            health=bg.get("health", 100),
            faction=bg.get("faction", Faction.NONE)
        )
        
        return self.player
    
    def get_current_events(self) -> List[dict]:
        """获取当前时代的历史事件"""
        events = HistoricalEvent.EVENTS.get(self.state.era, [])
        return [e for e in events if e["year"] <= self.state.year]
    
    def process_choice(self, choice: dict) -> str:
        """处理玩家选择"""
        effects = choice.get("effect", {})
        results = []
        
        for attr, value in effects.items():
            if hasattr(self.player, attr):
                current = getattr(self.player, attr)
                new_value = current + value
                setattr(self.player, attr, new_value)
                
                if value > 0:
                    results.append(f"{attr} +{value}")
                else:
                    results.append(f"{attr} {value}")
        
        return "，".join(results) if results else "无特殊影响"
    
    def advance_time(self, months: int = 1):
        """推进时间"""
        self.state.month += months
        while self.state.month > 12:
            self.state.month -= 12
            self.state.year += 1
            self.player.age += 1
        
        self._update_era()
        self.state.turn += 1
    
    def _update_era(self):
        """更新历史时期"""
        if self.state.year >= 1945:
            self.state.era = Era.CIVIL_WAR
        elif self.state.year >= 1937:
            self.state.era = Era.SINO_JAPANESE_WAR
        elif self.state.year >= 1928:
            self.state.era = Era.NANJING_DECADE
        else:
            self.state.era = Era.EARLY_REPUBLIC
    
    def generate_random_event(self) -> dict:
        """生成随机事件（未来接入AI）"""
        random_events = [
            {
                "type": "social",
                "description": "你收到了一封来自老友的邀请信，邀你参加文人聚会。",
                "choices": [
                    {"text": "欣然赴约", "effect": {"charisma": 5, "intelligence": 3}},
                    {"text": "婉言谢绝", "effect": {}},
                    {"text": "回信询问详情", "effect": {"intelligence": 2}}
                ]
            },
            {
                "type": "economic",
                "description": "市场上出现了一个投资机会：开设纺织厂。",
                "choices": [
                    {"text": "投资开厂 (花费500银元)", "effect": {"money": -500, "influence": 10}},
                    {"text": "观望市场", "effect": {}},
                    {"text": "寻找合伙人", "effect": {"charisma": 5}}
                ]
            },
            {
                "type": "political",
                "description": "有人邀请你加入一个秘密组织，声称要改变中国命运。",
                "choices": [
                    {"text": "加入组织", "effect": {"influence": 20, "health": -5}},
                    {"text": "礼貌拒绝", "effect": {}},
                    {"text": "举报此人", "effect": {"money": 100, "charisma": -10}}
                ]
            }
        ]
        
        return random.choice(random_events)
    
    def get_status(self) -> str:
        """获取当前状态"""
        if not self.player:
            return "尚未创建角色"
        
        return f"""
╔══════════════════════════════════════╗
║      《历史模拟器：民国》              ║
╠══════════════════════════════════════╣
║ 时间: {self.state.year}年{self.state.month}月                    
║ 时代: {self.state.era.value}           
║ 地点: {self.state.current_location}                  
╠══════════════════════════════════════╣
║ 【{self.player.name}】 {self.player.title}           
║ 年龄: {self.player.age}岁                            
║ 派系: {self.player.faction.value}                    
╠══════════════════════════════════════╣
║ 资产: {self.player.money:,} 银元                     
║ 影响力: {self.player.influence}                      
║ 军事: {self.player.military}                         
║ 智力: {self.player.intelligence}                     
║ 魅力: {self.player.charisma}                         
║ 健康: {self.player.health}                           
╚══════════════════════════════════════╝
"""
    
    def start(self):
        """开始游戏"""
        print("""
╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║              《 历 史 模 拟 器 ： 民 国 》                   ║
║                                                              ║
║         穿越到1912年，体验波澜壮阔的民国风云                 ║
║                                                              ║
║     • 扮演历史人物，影响中国命运                             ║
║     • AI驱动剧情，每次游戏都不同                             ║
║     • 真实历史事件，感受时代洪流                             ║
║                                                              ║
║                    [按回车开始游戏]                          ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
        """)
    
    def save_game(self, filepath: str = "save.json"):
        """保存游戏"""
        save_data = {
            "player": {
                "name": self.player.name,
                "title": self.player.title,
                "faction": self.player.faction.value,
                "money": self.player.money,
                "influence": self.player.influence,
                "military": self.player.military,
                "intelligence": self.player.intelligence,
                "charisma": self.player.charisma,
                "health": self.player.health,
                "age": self.player.age
            },
            "state": {
                "year": self.state.year,
                "month": self.state.month,
                "era": self.state.era.value,
                "location": self.state.current_location,
                "turn": self.state.turn
            },
            "timestamp": datetime.now().isoformat()
        }
        
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(save_data, f, ensure_ascii=False, indent=2)
        
        print(f"游戏已保存到 {filepath}")
    
    def load_game(self, filepath: str = "save.json"):
        """加载游戏"""
        with open(filepath, 'r', encoding='utf-8') as f:
            save_data = json.load(f)
        
        player_data = save_data["player"]
        self.player = Character(
            name=player_data["name"],
            title=player_data["title"],
            money=player_data["money"],
            influence=player_data["influence"],
            military=player_data["military"],
            intelligence=player_data["intelligence"],
            charisma=player_data["charisma"],
            health=player_data["health"],
            age=player_data["age"]
        )
        
        state_data = save_data["state"]
        self.state.year = state_data["year"]
        self.state.month = state_data["month"]
        self.state.current_location = state_data["location"]
        self.state.turn = state_data["turn"]
        self._update_era()
        
        print(f"游戏已加载，当前回合: {self.state.turn}")


def main():
    """主函数 - 演示游戏流程"""
    game = MinguoGame()
    game.start()
    
    game.create_character("李明远", "scholar")
    game.player.title = "北大教授"
    
    print(game.get_status())
    
    print("\n【历史事件】")
    event = game.generate_random_event()
    print(f"\n{event['description']}")
    print("\n可选行动：")
    for i, choice in enumerate(event['choices'], 1):
        print(f"  {i}. {choice['text']}")
    
    result = game.process_choice(event['choices'][0])
    print(f"\n你选择了: {event['choices'][0]['text']}")
    print(f"影响: {result}")
    
    game.advance_time(6)
    print(game.get_status())


if __name__ == '__main__':
    main()
