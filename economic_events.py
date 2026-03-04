# 历史模拟器：民国 - 经济事件库
"""
涵盖1912-1949年中国经济发展重大事件
"""

from typing import List
from dataclasses import dataclass
from datetime import date

@dataclass
class EconomicEvent:
    """经济事件数据结构"""
    event_id: str
    title: str
    date: date
    description: str
    impact: str
    tags: List[str]

ECONOMIC_EVENTS = [
    EconomicEvent(
        event_id="econ_1927_001",
        title="国民政府统一币制",
        date=date(1927, 3, 1),
        description="国民政府建立后推行币制改革，废除各地军阀发行的杂币，统一使用银元作为本位币。",
        impact="初步统一了货币体系，促进商业流通。",
        tags=["货币改革", "经济统一"]
    ),
    EconomicEvent(
        event_id="econ_1935_001",
        title="法币改革",
        date=date(1935, 11, 4),
        description="国民政府实行法币改革，废两改元，以中央、中国、交通三家银行发行的纸币为法定货币，禁止银元流通。",
        impact="统一货币，但为后来的通货膨胀埋下隐患。",
        tags=["法币改革", "货币政策"]
    ),
    EconomicEvent(
        event_id="econ_1937_001",
        title="抗战经济体制",
        date=date(1937, 7, 7),
        description="全面抗战爆发后，国民政府实施战时经济管制，沿海工业内迁，发展大后方经济。",
        impact="工业向西南转移，重庆成为战时经济中心。",
        tags=["战时经济", "工业内迁"]
    ),
    EconomicEvent(
        event_id="econ_1948_001",
        title="金圆券改革失败",
        date=date(1948, 8, 19),
        description="国民政府发行金圆券取代法币，规定1金圆券=法币300万元。但政府滥发货币，导致恶性通货膨胀。",
        impact="货币改革彻底失败，民众财富化为乌有，加速国民政府垮台。",
        tags=["金圆券", "恶性通胀", "经济崩溃"]
    ),
]

if __name__ == "__main__":
    print(f"经济事件库加载完成，共{len(ECONOMIC_EVENTS)}个事件")
