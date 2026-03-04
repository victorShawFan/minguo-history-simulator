from dataclasses import dataclass
from typing import List, Dict
from datetime import date

@dataclass
class GameMechanic:
    """游戏机制设定"""
    mechanic_id: str
    name: str
    description: str
    category: str  # 外交、军事、经济、文化、内政
    effects: Dict[str, int]  # 影响的数值变化

# 游戏核心机制库
GAME_MECHANICS = [
    GameMechanic(
        mechanic_id="MECH_001",
        name="外交斡旋",
        description="派遣外交使团与列强谈判，可能获得技术援助、贷款或领土让步。成功率取决于国家威望和外交能力。",
        category="外交",
        effects={"威望": 10, "外交关系": 20, "资金": 50000}
    ),
    
    GameMechanic(
        mechanic_id="MECH_002",
        name="军事改革",
        description="聘请外国军事顾问，改革军队编制和训练体系。需要大量资金投入，但可显著提升军队战斗力。",
        category="军事",
        effects={"军事实力": 25, "资金": -100000, "军队士气": 15}
    ),
    
    GameMechanic(
        mechanic_id="MECH_003",
        name="工业振兴计划",
        description="引进外资建设工厂，发展轻工业和重工业。需要稳定的政治环境和充足资金，可大幅提升国家经济。",
        category="经济",
        effects={"经济": 30, "资金": -80000, "民众支持": 10}
    ),
    
    GameMechanic(
        mechanic_id="MECH_004",
        name="新文化运动",
        description="支持知识分子推动思想启蒙，提倡白话文和科学精神。提升国民教育水平，但可能引发保守派反对。",
        category="文化",
        effects={"文化": 20, "教育": 25, "保守派支持": -15}
    ),
    
    GameMechanic(
        mechanic_id="MECH_005",
        name="铁路建设",
        description="修建铁路连接主要城市，促进经济发展和军事调动。需要巨额投资，但长期收益巨大。",
        category="经济",
        effects={"经济": 15, "交通": 30, "资金": -150000, "军事调动速度": 20}
    ),
]

@dataclass
class PlayerDecision:
    """玩家决策系统"""
    decision_id: str
    title: str
    description: str
    options: List[Dict[str, any]]  # 选项列表
    
# 关键决策事件
DECISIONS = [
    PlayerDecision(
        decision_id="DEC_001",
        title="日本提出二十一条要求（1915）",
        description="日本趁一战欧洲列强无暇东顾，向中国提出灭亡性的二十一条要求，企图独占中国。如何应对？",
        options=[
            {"label": "全部拒绝", "effects": {"日本关系": -50, "民众支持": 30, "战争风险": 80}},
            {"label": "部分接受", "effects": {"日本关系": -20, "民众支持": -30, "领土": -10}},
            {"label": "拖延谈判", "effects": {"日本关系": -10, "外交能力": 10, "时间": 6}}
        ]
    ),
    
    PlayerDecision(
        decision_id="DEC_002",
        title="是否参加一战（1917）",
        description="一战进入尾声，协约国邀请中国参战对抗同盟国。参战可能在战后和会上获得发言权，但需要派兵出国。",
        options=[
            {"label": "参战", "effects": {"国际地位": 20, "资金": -50000, "战后发言权": 30}},
            {"label": "中立", "effects": {"国际地位": -10, "经济": 10, "战后发言权": 0}},
            {"label": "向同盟国宣战但不派兵", "effects": {"国际地位": 5, "资金": -10000, "战后发言权": 10}}
        ]
    ),
]

def calculate_national_strength(attributes: Dict[str, int]) -> int:
    """计算国家综合实力"""
    weights = {
        "军事实力": 0.3,
        "经济": 0.3,
        "威望": 0.2,
        "民众支持": 0.1,
        "外交关系": 0.1
    }
    total = sum(attributes.get(key, 0) * weight for key, weight in weights.items())
    return int(total)
