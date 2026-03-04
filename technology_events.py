from dataclasses import dataclass
from datetime import date
from typing import List

@dataclass
class TechnologyEvent:
    """民国科技与工业事件"""
    event_id: str
    date: date
    title: str
    description: str
    category: str
    impact: int

TECHNOLOGY_EVENTS = [
    TechnologyEvent(
        event_id="TECH_001",
        date=date(1909, 9, 21),
        title="中国首条自主设计铁路：京张铁路通车",
        description="詹天佑主持设计的京张铁路通车，全长201公里。采用'人'字形铁路设计巧妙解决坡度难题，打破外国人'中国工程师无法修建铁路'的断言。",
        category="交通",
        impact=80
    ),
    
    TechnologyEvent(
        event_id="TECH_002",
        date=date(1919, 5, 4),
        title="北京大学成立科学研究所",
        description="蔡元培在北大成立科学研究所，聘请陈独秀、李大钊、胡适等学者，推动现代科学研究。",
        category="教育",
        impact=70
    ),
    
    TechnologyEvent(
        event_id="TECH_003",
        date=date(1935, 8, 1),
        title="中国航空工业起步",
        description="南京国民政府成立中央航空工业，建立飞机制造厂，仿制美国寇蒂斯战机。",
        category="军工",
        impact=60
    ),
]
