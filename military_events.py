from dataclasses import dataclass
from datetime import date
from typing import List, Dict, Optional

@dataclass
class MilitaryEvent:
    """民国军事战役事件"""
    event_id: str
    date: date
    title: str
    description: str
    location: str
    belligerents: Dict[str, List[str]]  # {"攻方": [...], "守方": [...]}
    commanders: Dict[str, List[str]]  # {"攻方": [...], "守方": [...]}
    forces: Dict[str, str]  # {"攻方": "兵力", "守方": "兵力"}
    casualties: Optional[Dict[str, str]]  # 伤亡情况
    result: str
    significance: str
    military_impact: int  # -100到100，负数表示对国家损害

# 民国重大军事战役数据库
MILITARY_EVENTS = [
    # 护国战争（反袁世凯称帝）
    MilitaryEvent(
        event_id="MIL_001",
        date=date(1915, 12, 25),
        title="护国战争爆发",
        description="袁世凯复辟帝制，蔡锷在云南宣布独立，组织护国军讨袁。随后贵州、广西响应，护国军分三路进攻四川、湖南。袁世凯北洋军虽装备精良，但军心涣散，屡战屡败。1916年3月袁世凯被迫取消帝制，6月忧郁而死。",
        location="云南、四川、贵州、广西",
        belligerents={
            "护国军": ["云南军、贵州军、广西军"],
            "北洋军": ["袁世凯中央军"]
        },
        commanders={
            "护国军": ["蔡锷", "唐继尧", "李烈钧"],
            "北洋军": ["曹锟", "张敬尧"]
        },
        forces={
            "护国军": "约3万人",
            "北洋军": "约15万人"
        },
        casualties={
            "护国军": "阵亡约5000人",
            "北洋军": "阵亡约8000人"
        },
        result="护国军胜利，袁世凯取消帝制后病死",
        significance="粉碎复辟帝制企图，维护共和制度，但加剧军阀割据",
        military_impact=60
    ),
    
    # 直皖战争
    MilitaryEvent(
        event_id="MIL_002",
        date=date(1920, 7, 14),
        title="直皖战争",
        description="直系曹锟、吴佩孚联合奉系张作霖，对抗控制北京政府的皖系段祺瑞。战争仅持续5天，皖系惨败。段祺瑞下台，直系控制北京政府。皖系'参战军'主力被歼灭，从此一蹶不振。",
        location="北京、天津、保定周边",
        belligerents={
            "直奉联军": ["直系军", "奉系军"],
            "皖系军": ["段祺瑞参战军"]
        },
        commanders={
            "直奉联军": ["曹锟", "吴佩孚", "张作霖"],
            "皖系军": ["段祺瑞", "徐树铮", "段芝贵"]
        },
        forces={
            "直奉联军": "约12万人",
            "皖系军": "约8万人"
        },
        casualties={
            "直奉联军": "阵亡约1000人",
            "皖系军": "阵亡约2000人，被俘1万余人"
        },
        result="直系大胜，皖系覆灭",
        significance="北洋军阀三大派系（直、皖、奉）中皖系退出历史舞台，直系控制中央",
        military_impact=-20
    ),
    
    # 第一次直奉战争
    MilitaryEvent(
        event_id="MIL_003",
        date=date(1922, 4, 29),
        title="第一次直奉战争",
        description="直皖战争后，直系独揽大权，奉系不满。张作霖以'恢复法统、惩办祸首'为名出兵关内。双方在山海关、秦皇岛激战，奉军因海军倒戈、补给困难战败，退回东北。吴佩孚威望达到顶峰，被誉为'常胜将军'。",
        location="山海关、秦皇岛、滦州",
        belligerents={
            "直系军": ["吴佩孚直军"],
            "奉系军": ["张作霖奉军"]
        },
        commanders={
            "直系军": ["吴佩孚", "曹锟", "王承斌"],
            "奉系军": ["张作霖", "张学良", "郭松龄"]
        },
        forces={
            "直系军": "约15万人",
            "奉系军": "约18万人"
        },
        casualties={
            "直系军": "阵亡约3000人",
            "奉系军": "阵亡约6000人"
        },
        result="直系获胜，奉系退回东北",
        significance="吴佩孚成为北洋最强军阀，但种下直奉矛盾，为二次大战埋下伏笔",
        military_impact=-15
    ),
    
    # 第二次直奉战争
    MilitaryEvent(
        event_id="MIL_004",
        date=date(1924, 9, 15),
        title="第二次直奉战争与北京政变",
        description="奉系张作霖整军再战，直奉两军在山海关再次大战。关键时刻，直系将领冯玉祥倒戈发动'北京政变'（又称'首都革命'），囚禁贿选总统曹锟，电邀孙中山北上商讨国是。吴佩孚腹背受敌，直系崩溃。奉系入主北京，张作霖成为北洋最后的统治者。",
        location="山海关、北京、天津",
        belligerents={
            "奉系军": ["张作霖奉军"],
            "直系军": ["吴佩孚直军（冯玉祥倒戈）"]
        },
        commanders={
            "奉系军": ["张作霖", "张学良", "张宗昌"],
            "直系军": ["吴佩孚", "曹锟（被囚）", "冯玉祥（倒戈）"]
        },
        forces={
            "奉系军": "约20万人",
            "直系军": "约25万人（冯玉祥倒戈带走5万）"
        },
        casualties={
            "奉系军": "阵亡约5000人",
            "直系军": "阵亡约8000人，被俘2万余人"
        },
        result="奉系大胜，直系瓦解，冯玉祥控制北京",
        significance="北洋军阀格局重组，张作霖入主北京，但南方国民革命势力崛起",
        military_impact=-25
    ),
    
    # 国民革命军北伐
    MilitaryEvent(
        event_id="MIL_005",
        date=date(1926, 7, 9),
        title="北伐战争开始",
        description="国民政府在广州誓师北伐，蒋介石任总司令。北伐军分三路：主力沿粤汉铁路北上攻湖南湖北，东路攻江西福建，西路固守两广。仅8个月攻克武汉、南昌、南京、上海，基本消灭吴佩孚、孙传芳两大军阀。北伐军战术先进，士气高昂，屡以少胜多。",
        location="湖南、湖北、江西、福建、浙江、江苏、安徽",
        belligerents={
            "国民革命军": ["黄埔军、湘军、粤军"],
            "北洋军阀": ["吴佩孚直军", "孙传芳五省联军"]
        },
        commanders={
            "国民革命军": ["蒋介石", "李济深", "白崇禧", "何应钦"],
            "北洋军阀": ["吴佩孚", "孙传芳", "张宗昌"]
        },
        forces={
            "国民革命军": "约10万人（后扩充至40万）",
            "北洋军阀": "约50万人"
        },
        casualties={
            "国民革命军": "阵亡约3万人",
            "北洋军阀": "阵亡约10万人，投降改编20万"
        },
        result="国民革命军大胜，占领长江流域",
        significance="推翻北洋军阀统治，国民政府定都南京，形式上统一中国（东北除外）",
        military_impact=80
    ),
    
    # 中原大战
    MilitaryEvent(
        event_id="MIL_006",
        date=date(1930, 5, 1),
        title="中原大战",
        description="冯玉祥、阎锡山、李宗仁联合反蒋，双方在河南、山东、湖北激战。投入总兵力超过130万，是民国史上规模最大的内战。战争持续半年，关键时刻张学良宣布'拥护中央'，东北军入关支持蒋介石，反蒋联军崩溃。此战死伤30万，耗资数亿，民穷财尽。",
        location="河南、山东、湖北、陕西",
        belligerents={
            "中央军": ["蒋介石中央军", "张学良东北军"],
            "反蒋联军": ["冯玉祥西北军", "阎锡山晋军", "李宗仁桂军"]
        },
        commanders={
            "中央军": ["蒋介石", "何应钦", "张学良"],
            "反蒋联军": ["冯玉祥", "阎锡山", "李宗仁"]
        },
        forces={
            "中央军": "约60万人（加东北军20万）",
            "反蒋联军": "约70万人"
        },
        casualties={
            "中央军": "阵亡约10万人",
            "反蒋联军": "阵亡约20万人"
        },
        result="蒋介石获胜，巩固统治",
        significance="国民政府基本统一全国（除西南地方实力派），但国力大损，为日后抗战埋下隐患",
        military_impact=-40
    ),
    
    # 一·二八淞沪抗战
    MilitaryEvent(
        event_id="MIL_007",
        date=date(1932, 1, 28),
        title="一·二八淞沪抗战",
        description="日军以'保护侨民'为名进攻上海，十九路军蔡廷锴、蒋光鼐奋起抵抗。第五军张治中部驰援。中国军队在闸北、江湾与日军激战33天，三次击退日军进攻。日军增兵至9万，动用海空军，中国军队伤亡惨重但士气高昂。最终国联调停，日军撤出上海市区，中国取得道义胜利。",
        location="上海闸北、江湾、吴淞",
        belligerents={
            "中国军队": ["十九路军", "第五军"],
            "日本侵略军": ["上海派遣军"]
        },
        commanders={
            "中国军队": ["蔡廷锴", "蒋光鼐", "张治中"],
            "日本侵略军": ["植田谦吉", "白川义则（被炸死）"]
        },
        forces={
            "中国军队": "约5万人",
            "日本侵略军": "约9万人（后增兵）"
        },
        casualties={
            "中国军队": "阵亡约1.4万人，伤2万人",
            "日本侵略军": "阵亡约3000人（日方公布），实际可能更高"
        },
        result="战术平局，日军暂时撤出上海市区",
        significance="中国军队首次大规模抵抗日本侵略，振奋民心，但南京政府仍坚持'攘外必先安内'",
        military_impact=50
    ),
    
    # 长城抗战
    MilitaryEvent(
        event_id="MIL_008",
        date=date(1933, 3, 9),
        title="长城抗战",
        description="日军占领东北后继续南侵，进攻长城各口（古北口、喜峰口、冷口等）。中国军队在宋哲元、张自忠、赵登禹等将领率领下浴血抵抗。大刀队夜袭日军阵地，砍杀日军数百人，威震敌胆。《大刀进行曲》由此诞生。但日军装备和火力占优，中国军队伤亡惨重，最终失守长城，日军逼近北平。",
        location="河北古北口、喜峰口、罗文峪",
        belligerents={
            "中国军队": ["宋哲元第29军", "关麟征第25师"],
            "日本侵略军": ["关东军"]
        },
        commanders={
            "中国军队": ["宋哲元", "张自忠", "赵登禹"],
            "日本侵略军": ["武藤信义", "铃木美通"]
        },
        forces={
            "中国军队": "约10万人",
            "日本侵略军": "约8万人"
        },
        casualties={
            "中国军队": "阵亡约2万人",
            "日本侵略军": "阵亡约5000人（日方公布），实际可能更高"
        },
        result="中国军队失守长城，日军占领热河、逼近平津",
        significance="中国军队英勇抵抗，大刀队夜袭震惊中外，但装备落后导致失败，《塘沽协定》签订",
        military_impact=-30
    ),
    
    # 八一三淞沪会战
    MilitaryEvent(
        event_id="MIL_009",
        date=date(1937, 8, 13),
        title="八一三淞沪会战",
        description="全面抗战爆发后，国民政府调集70万精锐在上海与日军决战，试图改变日军由北向南的进攻路线，吸引国际调停。中日双方投入百万兵力，激战3个月。中国空军、海军几乎全军覆没，陆军装备精良的中央军损失惨重（德械师几乎打光）。日军也伤亡4万余人，被迫从本土增兵。最终中国军队撤退，日军占领上海，南京门户大开。",
        location="上海及周边（罗店、宝山、大场、蕴藻浜）",
        belligerents={
            "中国军队": ["中央军、地方军阀部队"],
            "日本侵略军": ["上海派遣军、第10军"]
        },
        commanders={
            "中国军队": ["蒋介石（统帅）", "张治中", "薛岳", "陈诚"],
            "日本侵略军": ["松井石根", "柳川平助"]
        },
        forces={
            "中国军队": "约70万人（陆续投入）",
            "日本侵略军": "约30万人（陆续增兵）"
        },
        casualties={
            "中国军队": "阵亡、负伤、失踪约30万人",
            "日本侵略军": "阵亡、负伤约4万人（日方公布）"
        },
        result="中国军队战略撤退，日军占领上海",
        significance="粉碎日军'三个月灭亡中国'计划，但国军精锐损失殆尽，日军乘胜进攻南京",
        military_impact=-60
    ),
    
    # 台儿庄大捷
    MilitaryEvent(
        event_id="MIL_010",
        date=date(1938, 3, 23),
        title="台儿庄大捷",
        description="日军第5、第10师团沿津浦路南下，企图会师徐州。李宗仁指挥第五战区部队在台儿庄设伏，池峰城第31师死守台儿庄。激战半月，中国军队顽强抵抗，同时汤恩伯军团迂回日军侧后。日军陷入包围，损失惨重，被迫撤退。此战歼敌1万余人，缴获大批武器，是抗战以来最大胜利。",
        location="山东台儿庄",
        belligerents={
            "中国军队": ["第五战区部队"],
            "日本侵略军": ["第5师团、第10师团"]
        },
        commanders={
            "中国军队": ["李宗仁", "孙连仲", "池峰城", "汤恩伯"],
            "日本侵略军": ["矶谷廉介", "板垣征四郎"]
        },
        forces={
            "中国军队": "约30万人",
            "日本侵略军": "约5万人"
        },
        casualties={
            "中国军队": "阵亡约2万人，负伤约2万人",
            "日本侵略军": "阵亡约1万人（日方承认7000），负伤1万余人"
        },
        result="中国军队大胜，日军第10师团几乎被歼灭",
        significance="抗战以来正面战场最大胜利，振奋全国人心，粉碎'日军不可战胜'神话",
        military_impact=70
    ),
    
    # 武汉会战
    MilitaryEvent(
        event_id="MIL_011",
        date=date(1938, 6, 11),
        title="武汉会战",
        description="日军集结35万兵力分四路进攻武汉，国民政府调集110万军队防御。会战历时4个半月，遍及皖、赣、鄂、豫，是抗战中规模最大、时间最长的战役。著名的万家岭大捷歼敌一个师团。为争取时间，蒋介石下令炸开黄河花园口大堤，淹死日军数千，但也造成89万中国百姓死亡，数百万人逃难。最终武汉失守，但消耗日军有生力量，日本'速战速决'战略彻底破产。",
        location="湖北、安徽、江西、河南",
        belligerents={
            "中国军队": ["国民政府各战区部队"],
            "日本侵略军": ["第2军、第11军、华中派遣军"]
        },
        commanders={
            "中国军队": ["蒋介石（统帅）", "陈诚", "薛岳", "白崇禧"],
            "日本侵略军": ["畑俊六", "冈村宁次"]
        },
        forces={
            "中国军队": "约110万人",
            "日本侵略军": "约35万人"
        },
        casualties={
            "中国军队": "阵亡、负伤约25万人",
            "日本侵略军": "阵亡、负伤约10万人（日方公布3.5万，实际更高）"
        },
        result="日军占领武汉，但战略速决失败",
        significance="大量消耗日军，抗战进入相持阶段，日本陷入中国战场泥潭，但黄河决堤造成人道灾难",
        military_impact=-20
    ),
    
    # 昆仑关战役
    MilitaryEvent(
        event_id="MIL_012",
        date=date(1939, 12, 18),
        title="昆仑关战役",
        description="日军第5师团（号称'钢军'）攻占广西南宁、昆仑关，威胁西南大后方。蒋介石急调精锐第5军（杜聿明）、桂军（白崇禧）反攻。激战月余，中国军队付出重大伤亡夺回昆仑关，击毙日军'钢军之花'中村正雄少将旅团长。日军撤出南宁。此战是国军在桂南的重大胜利，但第5军伤亡过半。",
        location="广西昆仑关、南宁",
        belligerents={
            "中国军队": ["第5军（杜聿明）", "桂军"],
            "日本侵略军": ["第5师团（钢军）"]
        },
        commanders={
            "中国军队": ["白崇禧", "杜聿明", "戴安澜", "郑洞国"],
            "日本侵略军": ["今村均", "中村正雄（阵亡）"]
        },
        forces={
            "中国军队": "约15万人",
            "日本侵略军": "约2万人"
        },
        casualties={
            "中国军队": "阵亡约1.4万人，负伤2万余人",
            "日本侵略军": "阵亡约4000人（日方公布），含中村正雄少将"
        },
        result="中国军队收复昆仑关，日军撤出南宁",
        significance="国军首次攻坚战胜利，击毙日军少将，保卫西南大后方，但伤亡代价巨大",
        military_impact=50
    ),
]

def get_battles_by_period(start: date, end: date) -> List[MilitaryEvent]:
    """按时期筛选战役"""
    return [event for event in MILITARY_EVENTS if start <= event.date <= end]

def get_battles_by_location(location: str) -> List[MilitaryEvent]:
    """按地点筛选战役"""
    return [event for event in MILITARY_EVENTS if location in event.location]

def get_anti_japanese_battles() -> List[MilitaryEvent]:
    """获取所有抗日战役"""
    return [event for event in MILITARY_EVENTS 
            if "日本" in str(event.belligerents)]

def calculate_war_impact(events: List[MilitaryEvent]) -> Dict[str, float]:
    """计算战争影响评分"""
    total_impact = sum(e.military_impact for e in events)
    anti_japanese = [e for e in events if "日本" in str(e.belligerents)]
    civil_war = [e for e in events if "日本" not in str(e.belligerents)]
    
    return {
        "总体军事影响": total_impact,
        "抗日战争胜利": sum(e.military_impact for e in anti_japanese if e.military_impact > 0),
        "内战损耗": abs(sum(e.military_impact for e in civil_war if e.military_impact < 0)),
        "民族抵抗指数": len(anti_japanese) * 10
    }
