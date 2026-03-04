from dataclasses import dataclass
from datetime import date
from typing import List, Dict

@dataclass
class SocialEvent:
    """民国社会变革事件"""
    event_id: str
    date: date
    title: str
    description: str
    category: str  # 教育、女性解放、城市化、社会运动
    impact_regions: List[str]
    social_impact: int  # -100到100，表示社会进步程度
    affected_groups: List[str]  # 受影响的社会群体
    
# 民国重要社会事件数据库
SOCIAL_EVENTS = [
    # 教育改革事件
    SocialEvent(
        event_id="SOC_001",
        date=date(1912, 1, 19),
        title="蔡元培就任教育总长",
        description="蔡元培就任南京临时政府教育总长，提出'五育并举'教育方针（军国民教育、实利主义教育、公民道德教育、世界观教育、美感教育），主张教育独立、思想自由，废除读经科目，开民国教育改革先河。",
        category="教育",
        impact_regions=["全国"],
        social_impact=85,
        affected_groups=["学生", "知识分子", "教育工作者"]
    ),
    
    SocialEvent(
        event_id="SOC_002",
        date=date(1917, 1, 11),
        title="蔡元培主持北大改革",
        description="蔡元培出任北京大学校长，推行'思想自由，兼容并包'方针，聘任陈独秀、李大钊、胡适等新派人物，同时保留辜鸿铭等旧派学者，北大成为新文化运动中心。改革包括：废除学监制、整顿学风、提倡研究学术。",
        category="教育",
        impact_regions=["北京", "全国"],
        social_impact=90,
        affected_groups=["大学生", "知识分子", "青年"]
    ),
    
    SocialEvent(
        event_id="SOC_003",
        date=date(1922, 11, 1),
        title="壬戌学制实施",
        description="国民政府颁布'壬戌学制'（又称'六三三学制'：小学6年、初中3年、高中3年），取代清末'癸卯学制'，采用美国学制模式，确立现代教育体系基本框架，影响至今。增设选修课、职业教育，重视个性发展。",
        category="教育",
        impact_regions=["全国"],
        social_impact=80,
        affected_groups=["学生", "教师", "家长"]
    ),
    
    # 女性解放事件
    SocialEvent(
        event_id="SOC_004",
        date=date(1912, 3, 8),
        title="中华民国临时约法赋予女性参政权",
        description="《中华民国临时约法》颁布，虽未明确规定女性选举权，但唐群英等女权运动者冲击国会，要求'男女平权'。此后各省陆续允许女性参政，广东、湖南率先承认女性地方选举权。",
        category="女性解放",
        impact_regions=["广东", "湖南", "部分省份"],
        social_impact=70,
        affected_groups=["女性", "知识女性", "妇女运动者"]
    ),
    
    SocialEvent(
        event_id="SOC_005",
        date=date(1920, 9, 1),
        title="女子高等教育开放",
        description="北京大学、南京高等师范学校等开始招收女学生，打破千年来'女子无才便是德'传统。第一批女大学生包括王兰、韦均一等9人进入北大，开启女性接受高等教育先河。",
        category="女性解放",
        impact_regions=["北京", "南京", "上海"],
        social_impact=85,
        affected_groups=["女性", "知识女性", "学生"]
    ),
    
    SocialEvent(
        event_id="SOC_006",
        date=date(1924, 7, 15),
        title="妇女职业发展突破",
        description="上海、北京等大城市出现首批女性职业群体：女医生（张竹君）、女律师（郑毓秀，中国第一位女律师和女博士）、女教师、女记者。《妇女杂志》创刊，宣传女性权益和职业发展。",
        category="女性解放",
        impact_regions=["上海", "北京", "大城市"],
        social_impact=75,
        affected_groups=["职业女性", "城市女性"]
    ),
    
    SocialEvent(
        event_id="SOC_007",
        date=date(1927, 3, 8),
        title="武汉妇女运动高潮",
        description="国民革命军北伐期间，武汉成为妇女解放运动中心。向警予、邓颖超等领导'三八'妇女节大游行，数万妇女要求婚姻自由、废除童养媳、禁止缠足。武汉国民政府通过《妇女权利保障法》。",
        category="女性解放",
        impact_regions=["武汉", "湖北", "南方省份"],
        social_impact=80,
        affected_groups=["妇女", "农村女性", "工人"]
    ),
    
    # 城市化与现代生活
    SocialEvent(
        event_id="SOC_008",
        date=date(1914, 5, 1),
        title="上海现代都市生活兴起",
        description="上海成为远东第一大都市，现代设施完善：有轨电车、电灯、自来水、电话普及。南京路商业街繁荣，永安、先施等四大百货公司开业，咖啡馆、电影院、舞厅成为新时尚。",
        category="城市化",
        impact_regions=["上海"],
        social_impact=65,
        affected_groups=["城市居民", "中产阶级", "工商业者"]
    ),
    
    SocialEvent(
        event_id="SOC_009",
        date=date(1927, 5, 16),
        title="南京成为首都带动城市建设",
        description="国民政府定都南京，开展大规模城市建设：修建中山大道、中山陵，建设中央政府各部会大楼，规划新街口商业区。南京人口从30万增至百万，成为政治、文化中心。",
        category="城市化",
        impact_regions=["南京", "江苏"],
        social_impact=60,
        affected_groups=["南京居民", "建筑工人", "商人"]
    ),
    
    SocialEvent(
        event_id="SOC_010",
        date=date(1935, 10, 10),
        title="全国铁路网基本形成",
        description="民国铁路建设进入高峰，全国铁路总里程达21,000公里。京沪线、京汉线、陇海线、粤汉线等干线贯通，缩短城市间距离，促进人口流动和经济发展。火车成为主要交通工具。",
        category="城市化",
        impact_regions=["全国"],
        social_impact=75,
        affected_groups=["城市居民", "商人", "务工人员"]
    ),
    
    # 社会运动事件
    SocialEvent(
        event_id="SOC_011",
        date=date(1915, 9, 15),
        title="新文化运动开启",
        description="陈独秀在上海创办《青年杂志》（后改名《新青年》），提出'民主与科学'口号（德先生Mr. Democracy、赛先生Mr. Science），批判封建礼教，倡导白话文，掀起思想解放运动。",
        category="社会运动",
        impact_regions=["上海", "北京", "全国"],
        social_impact=95,
        affected_groups=["知识分子", "青年学生", "城市居民"]
    ),
    
    SocialEvent(
        event_id="SOC_012",
        date=date(1919, 5, 4),
        title="五四运动爆发",
        description="北京学生3000余人在天安门集会，抗议巴黎和会将德国在山东权益转给日本，提出'外争主权、内除国贼'口号。运动扩展至全国，工人罢工、商人罢市，最终迫使政府拒签和约。新文化运动进入新阶段。",
        category="社会运动",
        impact_regions=["全国"],
        social_impact=100,
        affected_groups=["学生", "工人", "商人", "知识分子"]
    ),
    
    SocialEvent(
        event_id="SOC_013",
        date=date(1925, 5, 30),
        title="五卅运动",
        description="上海日商纱厂枪杀工人顾正红，引发全国反帝爱国运动。5月30日上海学生在租界抗议被捕，英国巡捕开枪，死伤数十人。罢工、罢课、罢市席卷全国，历时3个月，沉重打击帝国主义在华势力。",
        category="社会运动",
        impact_regions=["上海", "全国"],
        social_impact=90,
        affected_groups=["工人", "学生", "市民"]
    ),
    
    SocialEvent(
        event_id="SOC_014",
        date=date(1936, 11, 22),
        title="救亡运动兴起",
        description="'一二·九运动'后，抗日救亡成为全国主题。各地成立'救国会'，知识分子、学生、工人组织抗日义勇军，开展募捐、宣传。上海'七君子'（沈钧儒、邹韬奋等）因救亡活动被捕，引发全国声援。",
        category="社会运动",
        impact_regions=["全国"],
        social_impact=85,
        affected_groups=["学生", "知识分子", "工人", "市民"]
    ),
    
    # 生活方式变迁
    SocialEvent(
        event_id="SOC_015",
        date=date(1912, 2, 14),
        title="剪辫易服运动",
        description="民国成立后，孙中山下令禁止蓄辫，鼓励穿西服、中山装。城市男性纷纷剪去辫子，女性开始解放缠足。服饰从长袍马褂转向西装、旗袍，象征告别帝制迎接共和。",
        category="生活方式",
        impact_regions=["城市地区"],
        social_impact=70,
        affected_groups=["城市居民", "知识分子"]
    ),
    
    SocialEvent(
        event_id="SOC_016",
        date=date(1929, 4, 20),
        title="国语运动推广",
        description="国民政府推行'国语统一运动'，以北京话为基础推广普通话（当时称'国语'）。设立国语推行委员会，编写《国音常用字汇》，在学校推行注音符号（ㄅㄆㄇㄈ），促进全国语言统一。",
        category="生活方式",
        impact_regions=["全国"],
        social_impact=75,
        affected_groups=["学生", "教师", "公务员"]
    ),
    
    SocialEvent(
        event_id="SOC_017",
        date=date(1934, 2, 19),
        title="新生活运动",
        description="蒋介石在南昌发起'新生活运动'，提倡'礼义廉耻'和'整齐、清洁、简单、朴素、迅速、确实'的生活原则。要求民众改变随地吐痰、乱扔垃圾等陋习，提倡守时、守法、公共卫生。运动在城市取得一定效果。",
        category="生活方式",
        impact_regions=["江西", "城市地区"],
        social_impact=55,
        affected_groups=["城市居民", "公务员"]
    ),
]

def get_events_by_category(category: str) -> List[SocialEvent]:
    """按类别筛选社会事件"""
    return [event for event in SOCIAL_EVENTS if event.category == category]

def get_events_by_date_range(start: date, end: date) -> List[SocialEvent]:
    """按日期范围筛选社会事件"""
    return [event for event in SOCIAL_EVENTS if start <= event.date <= end]

def get_events_affecting_group(group: str) -> List[SocialEvent]:
    """获取影响特定社会群体的事件"""
    return [event for event in SOCIAL_EVENTS if group in event.affected_groups]

# 社会指标计算
def calculate_modernization_score(events: List[SocialEvent]) -> Dict[str, float]:
    """计算社会现代化程度评分"""
    education_score = sum(e.social_impact for e in events if e.category == "教育") / 10
    womens_rights_score = sum(e.social_impact for e in events if e.category == "女性解放") / 10
    urbanization_score = sum(e.social_impact for e in events if e.category == "城市化") / 10
    
    return {
        "教育现代化": min(100, education_score),
        "女性权益": min(100, womens_rights_score),
        "城市化水平": min(100, urbanization_score),
        "社会总体进步": min(100, (education_score + womens_rights_score + urbanization_score) / 3)
    }
