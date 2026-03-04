# 历史模拟器：民国 - 外交事件库
"""
涵盖1912-1949年中国外交史重大事件
数据来源：百科、历史文献
"""

from typing import List
from dataclasses import dataclass
from datetime import date

@dataclass
class DiplomaticEvent:
    """外交事件数据结构"""
    event_id: str
    title: str
    date: date
    description: str
    participants: List[str]  # 参与国家/组织
    key_figures: List[str]
    outcome: str  # 结果/影响
    tags: List[str]

DIPLOMATIC_EVENTS = [
    DiplomaticEvent(
        event_id="diplo_1919_001",
        title="巴黎和会中国外交失败",
        date=date(1919, 1, 18),
        description="第一次世界大战后，中国作为战胜国参加巴黎和会，提出收回山东主权等正当要求，但列强无视中国诉求，将德国在山东的权益转让给日本，史称'山东问题'。中国代表团拒绝在《凡尔赛和约》上签字。",
        participants=["中国", "日本", "英国", "法国", "美国"],
        key_figures=["顾维钧", "陆征祥", "威尔逊"],
        outcome="中国外交失败，直接引发五四运动。但中国代表拒绝签字，展示了民族觉醒。",
        tags=["巴黎和会", "山东问题", "外交失败"]
    ),
    DiplomaticEvent(
        event_id="diplo_1921_001",
        title="华盛顿会议与九国公约",
        date=date(1921, 11, 12),
        description="美国召集华盛顿会议，签署《九国公约》，规定尊重中国主权独立与领土完整，但实际是列强共同宰割中国的新形式，日本被迫归还山东主权。",
        participants=["中国", "美国", "英国", "日本", "法国", "意大利", "荷兰", "比利时", "葡萄牙"],
        key_figures=["顾维钧", "王宠惠"],
        outcome="形式上维护中国主权，实际确立列强在华共同控制。日本归还山东，但中国仍受列强压制。",
        tags=["华盛顿会议", "九国公约", "山东归还"]
    ),
    DiplomaticEvent(
        event_id="diplo_1924_001",
        title="中苏建交",
        date=date(1924, 5, 31),
        description="北洋政府与苏联签订《中俄解决悬案大纲协定》，承认苏联放弃帝俄在华特权，两国正式建交。这是中国与第一个社会主义国家建立外交关系。",
        participants=["中国", "苏联"],
        key_figures=["顾维钧", "加拉罕"],
        outcome="苏联承诺放弃庚子赔款，归还中东铁路，支持中国革命。为国共合作和北伐奠定基础。",
        tags=["中苏建交", "平等外交"]
    ),
    DiplomaticEvent(
        event_id="diplo_1931_001",
        title="九一八事变后国联调查",
        date=date(1932, 10, 2),
        description="九一八事变后，中国向国际联盟申诉。国联派出李顿调查团，发布《李顿报告》认定日本侵略，但未采取实质制裁。日本退出国联。",
        participants=["中国", "日本", "国际联盟"],
        key_figures=["李顿", "顾维钧", "松冈洋右"],
        outcome="国联软弱无力，日本退出国联继续侵华。中国认识到'公理不敌强权'。",
        tags=["九一八", "国联", "李顿调查团"]
    ),
    DiplomaticEvent(
        event_id="diplo_1943_001",
        title="开罗会议",
        date=date(1943, 11, 22),
        description="中美英三国首脑在开罗举行会议，发表《开罗宣言》，明确战后日本窃取的中国领土（包括台湾、澎湖列岛、东北）必须归还中国。",
        participants=["中国", "美国", "英国"],
        key_figures=["蒋介石", "罗斯福", "丘吉尔"],
        outcome="确立战后台湾回归中国，提升中国国际地位，中国成为'四大国'之一。",
        tags=["开罗会议", "台湾回归", "四大国"]
    ),
    DiplomaticEvent(
        event_id="diplo_1945_001",
        title="联合国成立中国成为五常",
        date=date(1945, 6, 26),
        description="《联合国宪章》在旧金山签署，中国成为联合国创始会员国及安全理事会五个常任理事国之一，拥有否决权。",
        participants=["中国", "美国", "苏联", "英国", "法国", "及其他46国"],
        key_figures=["宋子文", "顾维钧"],
        outcome="中国首次以大国身份参与战后国际秩序建立，国际地位空前提高。",
        tags=["联合国", "五常", "国际地位"]
    ),
    DiplomaticEvent(
        event_id="diplo_1945_002",
        title="中苏友好同盟条约",
        date=date(1945, 8, 14),
        description="抗战胜利前夕，国民政府与苏联签订《中苏友好同盟条约》，苏联承认国民政府为中国唯一合法政府，但中国被迫承认外蒙古独立，苏联获得旅顺大连特权。",
        participants=["中国", "苏联"],
        key_figures=["宋子文", "斯大林"],
        outcome="确保苏联对日作战，但牺牲外蒙古主权，引发争议。",
        tags=["中苏条约", "外蒙古", "雅尔塔体系"]
    ),
]

def get_diplomatic_events_by_year(year: int) -> List[DiplomaticEvent]:
    """根据年份获取外交事件"""
    return [e for e in DIPLOMATIC_EVENTS if e.date.year == year]

def get_events_by_country(country: str) -> List[DiplomaticEvent]:
    """根据国家获取相关外交事件"""
    return [e for e in DIPLOMATIC_EVENTS if country in e.participants]

if __name__ == "__main__":
    print(f"外交事件库加载完成，共{len(DIPLOMATIC_EVENTS)}个事件")
    print("\n按时间排序：")
    for event in DIPLOMATIC_EVENTS:
        print(f"{event.date.strftime('%Y年%m月%d日')}: {event.title}")
