# 历史模拟器：民国 - 扩展历史事件库
"""
基于真实历史的事件库，覆盖1912-1949年重要历史节点
数据来源：今日头条《民国史全景》、《中华民国大事年表》等
"""

from typing import Dict, List, Optional
from dataclasses import dataclass
from datetime import date

@dataclass
class HistoricalEvent:
    """历史事件数据结构"""
    event_id: str
    title: str
    date: date
    description: str
    era: str  # EARLY_REPUBLIC | NANJING_DECADE | SINO_JAPANESE_WAR | CIVIL_WAR
    key_figures: List[str]
    locations: List[str]
    impact_level: int  # 1-5，5为最高影响力
    tags: List[str]

# 1912-1928 北洋时期重大事件
EARLY_REPUBLIC_EVENTS = [
    HistoricalEvent(
        event_id="1912_001",
        title="中华民国成立",
        date=date(1912, 1, 1),
        description="1912年1月1日，孙中山在南京宣誓就任中华民国临时大总统，发表《临时大总统就职宣言》，中华民国正式宣告成立。这标志着中国两千多年的封建帝制走向终结，共和政体正式建立。",
        era="EARLY_REPUBLIC",
        key_figures=["孙中山", "黄兴", "宋教仁"],
        locations=["南京"],
        impact_level=5,
        tags=["辛亥革命", "共和", "建国"]
    ),
    HistoricalEvent(
        event_id="1912_002",
        title="南北议和与清帝退位",
        date=date(1912, 2, 12),
        description="经过南北双方多轮谈判，1912年2月12日清帝溥仪颁布退位诏书，宣布退位。袁世凯通过与革命党的谈判，获得临时大总统职位，南北议和成功。",
        era="EARLY_REPUBLIC",
        key_figures=["袁世凯", "隆裕太后", "孙中山"],
        locations=["北京", "南京"],
        impact_level=5,
        tags=["清帝退位", "南北议和", "权力交接"]
    ),
    HistoricalEvent(
        event_id="1912_003",
        title="临时政府迁都北京",
        date=date(1912, 3, 10),
        description="为实现南北统一，孙中山辞去临时大总统职务，袁世凯在北京就任第二任临时大总统。临时政府正式从南京迁至北京，北洋政府时期开始。",
        era="EARLY_REPUBLIC",
        key_figures=["袁世凯", "孙中山"],
        locations=["北京", "南京"],
        impact_level=4,
        tags=["迁都", "北洋政府", "权力转移"]
    ),
    HistoricalEvent(
        event_id="1913_001",
        title="宋教仁遇刺案",
        date=date(1913, 3, 20),
        description="国民党领袖宋教仁在上海火车站准备北上就任内阁总理时遭枪击，两天后不治身亡。此案震惊全国，被认为是袁世凯指使，成为二次革命的导火索。",
        era="EARLY_REPUBLIC",
        key_figures=["宋教仁", "袁世凯", "孙中山"],
        locations=["上海"],
        impact_level=4,
        tags=["政治暗杀", "二次革命前奏"]
    ),
    HistoricalEvent(
        event_id="1913_002",
        title="二次革命爆发",
        date=date(1913, 7, 12),
        description="宋教仁遇刺后，国民党人发起反袁武装起义，史称'二次革命'。江西、安徽、江苏、广东、福建、湖南、四川七省先后宣布独立，但最终被袁世凯的北洋军镇压。",
        era="EARLY_REPUBLIC",
        key_figures=["孙中山", "黄兴", "袁世凯"],
        locations=["南京", "江西", "上海"],
        impact_level=3,
        tags=["武装起义", "反袁运动"]
    ),
    HistoricalEvent(
        event_id="1915_001",
        title="袁世凯称帝",
        date=date(1915, 12, 12),
        description="袁世凯在日本提出'二十一条'后国内声望大跌，但仍一意孤行宣布恢复帝制，改国号为'中华帝国'，改元洪宪。此举遭到全国上下强烈反对。",
        era="EARLY_REPUBLIC",
        key_figures=["袁世凯", "蔡锷", "梁启超"],
        locations=["北京"],
        impact_level=5,
        tags=["帝制复辟", "洪宪帝制"]
    ),
    HistoricalEvent(
        event_id="1915_002",
        title="护国战争爆发",
        date=date(1915, 12, 25),
        description="云南将领蔡锷、唐继尧等发起护国运动，宣布云南独立，组织护国军讨伐袁世凯。贵州、广西等省纷纷响应，袁世凯被迫于1916年3月22日宣布取消帝制。",
        era="EARLY_REPUBLIC",
        key_figures=["蔡锷", "唐继尧", "袁世凯"],
        locations=["云南", "贵州", "四川"],
        impact_level=4,
        tags=["护国运动", "反帝制"]
    ),
    HistoricalEvent(
        event_id="1916_001",
        title="袁世凯病逝与军阀混战开始",
        date=date(1916, 6, 6),
        description="洪宪帝制失败后，袁世凯于1916年6月6日因尿毒症病逝。其死后北洋军阀分裂为直系、皖系、奉系，中国进入长达十余年的军阀混战时期。",
        era="EARLY_REPUBLIC",
        key_figures=["袁世凯", "黎元洪", "段祺瑞"],
        locations=["北京"],
        impact_level=5,
        tags=["袁世凯之死", "军阀割据", "政局动荡"]
    ),
    HistoricalEvent(
        event_id="1917_001",
        title="张勋复辟",
        date=date(1917, 7, 1),
        description="辫子军阀张勋率5000辫子兵进入北京，扶持溥仪重新登基，企图恢复清朝。但复辟仅维持12天就在段祺瑞组织的讨逆军进攻下瓦解。",
        era="EARLY_REPUBLIC",
        key_figures=["张勋", "溥仪", "段祺瑞"],
        locations=["北京"],
        impact_level=3,
        tags=["复辟闹剧", "张勋复辟"]
    ),
    HistoricalEvent(
        event_id="1919_001",
        title="五四运动",
        date=date(1919, 5, 4),
        description="巴黎和会中国外交失败，北京学生在天安门前集会，高喊'外争主权，内除国贼'，火烧赵家楼，痛打章宗祥。运动迅速扩展到全国，标志着中国新民主主义革命的开端。",
        era="EARLY_REPUBLIC",
        key_figures=["陈独秀", "胡适", "李大钊"],
        locations=["北京", "上海", "天津"],
        impact_level=5,
        tags=["学生运动", "新文化运动", "反帝爱国"]
    ),
    HistoricalEvent(
        event_id="1921_001",
        title="中国共产党成立",
        date=date(1921, 7, 23),
        description="中国共产党第一次全国代表大会在上海秘密召开，后转移至浙江嘉兴南湖的游船上完成。大会通过党纲，选举陈独秀为中央局书记，标志着中国共产党正式成立。",
        era="EARLY_REPUBLIC",
        key_figures=["陈独秀", "李大钊", "毛泽东", "董必武"],
        locations=["上海", "嘉兴"],
        impact_level=5,
        tags=["建党伟业", "共产党成立", "马克思主义"]
    ),
    HistoricalEvent(
        event_id="1924_001",
        title="第一次国共合作",
        date=date(1924, 1, 20),
        description="国民党第一次全国代表大会在广州召开，通过新的党纲党章，确立'联俄、联共、扶助农工'三大政策，标志着第一次国共合作正式形成。",
        era="EARLY_REPUBLIC",
        key_figures=["孙中山", "李大钊", "毛泽东"],
        locations=["广州"],
        impact_level=4,
        tags=["国共合作", "统一战线"]
    ),
    HistoricalEvent(
        event_id="1926_001",
        title="北伐战争开始",
        date=date(1926, 7, 9),
        description="国民革命军在广州誓师北伐，以蒋介石为总司令，目标是打倒帝国主义支持的北洋军阀。北伐军分三路向北推进，战况顺利。",
        era="EARLY_REPUBLIC",
        key_figures=["蒋介石", "叶挺", "贺龙"],
        locations=["广州", "湖南", "武汉"],
        impact_level=5,
        tags=["北伐战争", "国民革命"]
    ),
    HistoricalEvent(
        event_id="1927_001",
        title="四一二反革命政变",
        date=date(1927, 4, 12),
        description="蒋介石在上海发动清党，大肆逮捕屠杀共产党员和革命群众，第一次国共合作彻底破裂，中国革命进入十年内战时期。",
        era="EARLY_REPUBLIC",
        key_figures=["蒋介石", "汪精卫", "陈独秀"],
        locations=["上海", "南京"],
        impact_level=5,
        tags=["反革命政变", "国共分裂", "白色恐怖"]
    ),
]

# 1928-1937 南京十年事件
NANJING_DECADE_EVENTS = [
    HistoricalEvent(
        event_id="1928_001",
        title="东北易帜",
        date=date(1928, 12, 29),
        description="张学良宣布东北服从南京国民政府，降下北洋政府的五色旗，升起青天白日满地红旗，史称'东北易帜'。至此，国民政府形式上统一全国。",
        era="NANJING_DECADE",
        key_figures=["张学良", "蒋介石"],
        locations=["沈阳"],
        impact_level=4,
        tags=["统一", "东北易帜"]
    ),
    HistoricalEvent(
        event_id="1931_001",
        title="九一八事变",
        date=date(1931, 9, 18),
        description="日本关东军在沈阳制造柳条湖事件，随后炮轰北大营，全面侵占东北。蒋介石下令'绝对不抵抗'，张学良率东北军撤入关内，东北三省迅速沦陷。",
        era="NANJING_DECADE",
        key_figures=["张学良", "蒋介石", "石原莞尔"],
        locations=["沈阳", "长春", "哈尔滨"],
        impact_level=5,
        tags=["日本侵华", "九一八", "东北沦陷"]
    ),
    HistoricalEvent(
        event_id="1932_001",
        title="一二八淞沪抗战",
        date=date(1932, 1, 28),
        description="日军进攻上海，十九路军奋起抵抗，与日军血战33天。这是中国军队首次大规模抗日作战，极大鼓舞了全国抗日士气。",
        era="NANJING_DECADE",
        key_figures=["蒋光鼐", "蔡廷锴", "张治中"],
        locations=["上海"],
        impact_level=4,
        tags=["淞沪抗战", "十九路军", "抗日"]
    ),
    HistoricalEvent(
        event_id="1934_001",
        title="红军长征开始",
        date=date(1934, 10, 10),
        description="由于第五次反围剿失败，中央红军被迫进行战略转移，从江西瑞金出发开始长征。历时两年，行程二万五千里，最终抵达陕北。",
        era="NANJING_DECADE",
        key_figures=["毛泽东", "周恩来", "朱德"],
        locations=["江西瑞金", "遵义", "延安"],
        impact_level=5,
        tags=["长征", "战略转移"]
    ),
    HistoricalEvent(
        event_id="1935_001",
        title="遵义会议",
        date=date(1935, 1, 15),
        description="红军长征途中在遵义召开政治局扩大会议，确立了毛泽东在党和红军中的领导地位，成为中国革命的转折点。",
        era="NANJING_DECADE",
        key_figures=["毛泽东", "周恩来", "朱德"],
        locations=["贵州遵义"],
        impact_level=5,
        tags=["遵义会议", "历史转折"]
    ),
    HistoricalEvent(
        event_id="1936_001",
        title="西安事变",
        date=date(1936, 12, 12),
        description="张学良、杨虎城在西安发动兵谏，扣押蒋介石，要求停止内战、一致抗日。经过谈判，蒋介石接受停止内战、联共抗日的主张，西安事变和平解决。",
        era="NANJING_DECADE",
        key_figures=["张学良", "杨虎城", "蒋介石", "周恩来"],
        locations=["西安"],
        impact_level=5,
        tags=["西安事变", "兵谏", "抗日统一战线"]
    ),
]

# 1937-1945 抗日战争事件
SINO_JAPANESE_WAR_EVENTS = [
    HistoricalEvent(
        event_id="1937_001",
        title="七七事变",
        date=date(1937, 7, 7),
        description="日军在卢沟桥制造事端，向中国守军开火，第29军奋起抵抗。这标志着全面抗日战争的爆发，中国进入八年抗战时期。",
        era="SINO_JAPANESE_WAR",
        key_figures=["佟麟阁", "赵登禹", "宋哲元"],
        locations=["北平卢沟桥"],
        impact_level=5,
        tags=["七七事变", "卢沟桥", "全面抗战"]
    ),
    HistoricalEvent(
        event_id="1937_002",
        title="淞沪会战",
        date=date(1937, 8, 13),
        description="中日两国在上海及周边地区展开长达三个月的激战，中国军队投入70余万兵力，伤亡30余万。虽然战役失利，但打破了日本'三个月灭亡中国'的狂言。",
        era="SINO_JAPANESE_WAR",
        key_figures=["蒋介石", "张治中", "谢晋元"],
        locations=["上海"],
        impact_level=5,
        tags=["淞沪会战", "四行仓库", "抗日战争"]
    ),
    HistoricalEvent(
        event_id="1937_003",
        title="南京大屠杀",
        date=date(1937, 12, 13),
        description="日军攻陷南京后，进行了长达六周的大规模屠杀、强奸、抢劫、纵火。据战后远东国际军事法庭统计，死难者达30万人以上。",
        era="SINO_JAPANESE_WAR",
        key_figures=["松井石根", "唐生智", "约翰·拉贝"],
        locations=["南京"],
        impact_level=5,
        tags=["南京大屠杀", "战争罪行", "国家公祭日"]
    ),
    HistoricalEvent(
        event_id="1938_001",
        title="台儿庄大捷",
        date=date(1938, 3, 23),
        description="中国军队在山东台儿庄重创日军两个精锐师团，歼敌1万余人，这是抗战以来正面战场取得的最大胜利，极大鼓舞了全国抗战士气。",
        era="SINO_JAPANESE_WAR",
        key_figures=["李宗仁", "张自忠", "孙连仲"],
        locations=["山东台儿庄"],
        impact_level=4,
        tags=["台儿庄大捷", "正面战场"]
    ),
    HistoricalEvent(
        event_id="1940_001",
        title="百团大战",
        date=date(1940, 8, 20),
        description="八路军在华北地区对日军发动的一次大规模进攻战役，参战部队达105个团，破坏日军交通线、据点，沉重打击了日军'囚笼政策'。",
        era="SINO_JAPANESE_WAR",
        key_figures=["彭德怀", "左权", "聂荣臻"],
        locations=["山西", "河北"],
        impact_level=4,
        tags=["百团大战", "敌后战场"]
    ),
    HistoricalEvent(
        event_id="1945_001",
        title="日本投降",
        date=date(1945, 8, 15),
        description="美国向广岛、长崎投下原子弹后，日本宣布无条件投降。8月15日，日本天皇发表《终战诏书》，中国抗日战争胜利结束。",
        era="SINO_JAPANESE_WAR",
        key_figures=["蒋介石", "毛泽东", "裕仁天皇"],
        locations=["东京", "重庆", "延安"],
        impact_level=5,
        tags=["抗战胜利", "日本投降", "终战"]
    ),
]

# 1945-1949 解放战争事件
CIVIL_WAR_EVENTS = [
    HistoricalEvent(
        event_id="1945_002",
        title="重庆谈判",
        date=date(1945, 8, 29),
        description="抗战胜利后，毛泽东应蒋介石邀请赴重庆谈判，双方签署《双十协定》，但国共双方对政权归属仍存在根本分歧。",
        era="CIVIL_WAR",
        key_figures=["毛泽东", "蒋介石", "周恩来"],
        locations=["重庆"],
        impact_level=4,
        tags=["重庆谈判", "和平谈判"]
    ),
    HistoricalEvent(
        event_id="1946_001",
        title="全面内战爆发",
        date=date(1946, 6, 26),
        description="国民党军队大举进攻中原解放区，全面内战爆发。人民解放军实施战略防御，以运动战为主要作战方式。",
        era="CIVIL_WAR",
        key_figures=["蒋介石", "毛泽东", "李先念"],
        locations=["中原", "山东"],
        impact_level=5,
        tags=["内战爆发", "解放战争"]
    ),
    HistoricalEvent(
        event_id="1947_001",
        title="三大战役：辽沈战役",
        date=date(1948, 9, 12),
        description="人民解放军在东北进行战略决战，历时52天，歼灭国民党军47万余人，解放东北全境。林彪、罗荣桓指挥东北野战军取得完胜。",
        era="CIVIL_WAR",
        key_figures=["林彪", "罗荣桓", "卫立煌"],
        locations=["辽宁", "沈阳", "锦州"],
        impact_level=5,
        tags=["辽沈战役", "三大战役", "东北解放"]
    ),
    HistoricalEvent(
        event_id="1948_002",
        title="三大战役：淮海战役",
        date=date(1948, 11, 6),
        description="华东野战军和中原野战军在徐州地区进行战略决战，历时66天，歼敌55万余人。陈毅评价：'淮海战役是老百姓用小推车推出来的胜利'。",
        era="CIVIL_WAR",
        key_figures=["刘伯承", "邓小平", "陈毅", "粟裕"],
        locations=["徐州", "安徽"],
        impact_level=5,
        tags=["淮海战役", "三大战役", "决战"]
    ),
    HistoricalEvent(
        event_id="1948_003",
        title="三大战役：平津战役",
        date=date(1948, 11, 29),
        description="东北野战军和华北军区部队联合作战，和平解放北平（今北京），歼敌52万余人。傅作义率部起义，北平古城免遭战火破坏。",
        era="CIVIL_WAR",
        key_figures=["林彪", "聂荣臻", "傅作义"],
        locations=["北平", "天津", "张家口"],
        impact_level=5,
        tags=["平津战役", "三大战役", "和平解放"]
    ),
    HistoricalEvent(
        event_id="1949_001",
        title="渡江战役与解放南京",
        date=date(1949, 4, 21),
        description="人民解放军发起渡江战役，百万雄师横渡长江，4月23日攻占南京，国民党在大陆的统治宣告结束。",
        era="CIVIL_WAR",
        key_figures=["毛泽东", "朱德", "蒋介石"],
        locations=["南京", "长江"],
        impact_level=5,
        tags=["渡江战役", "解放南京", "胜利"]
    ),
    HistoricalEvent(
        event_id="1949_002",
        title="开国大典",
        date=date(1949, 10, 1),
        description="中华人民共和国开国大典在北京天安门广场隆重举行。毛泽东主席宣告：'中华人民共和国中央人民政府今天成立了！'",
        era="CIVIL_WAR",
        key_figures=["毛泽东", "周恩来", "朱德"],
        locations=["北京天安门"],
        impact_level=5,
        tags=["开国大典", "新中国成立", "历史转折"]
    ),
]

# 合并所有事件
ALL_HISTORICAL_EVENTS = (
    EARLY_REPUBLIC_EVENTS +
    NANJING_DECADE_EVENTS +
    SINO_JAPANESE_WAR_EVENTS +
    CIVIL_WAR_EVENTS
)

def get_events_by_era(era: str) -> List[HistoricalEvent]:
    """根据时代获取事件列表"""
    return [event for event in ALL_HISTORICAL_EVENTS if event.era == era]

def get_events_by_year(year: int) -> List[HistoricalEvent]:
    """根据年份获取事件列表"""
    return [event for event in ALL_HISTORICAL_EVENTS if event.date.year == year]

def get_event_by_id(event_id: str) -> Optional[HistoricalEvent]:
    """根据ID获取事件"""
    for event in ALL_HISTORICAL_EVENTS:
        if event.event_id == event_id:
            return event
    return None

def get_events_by_figure(figure_name: str) -> List[HistoricalEvent]:
    """根据历史人物获取相关事件"""
    return [event for event in ALL_HISTORICAL_EVENTS if figure_name in event.key_figures]

def search_events(keyword: str) -> List[HistoricalEvent]:
    """关键词搜索事件"""
    results = []
    keyword_lower = keyword.lower()
    for event in ALL_HISTORICAL_EVENTS:
        if (keyword_lower in event.title.lower() or
            keyword_lower in event.description.lower() or
            any(keyword_lower in tag.lower() for tag in event.tags)):
            results.append(event)
    return results

if __name__ == "__main__":
    print(f"历史事件库加载完成，共{len(ALL_HISTORICAL_EVENTS)}个事件")
    print(f"北洋时期: {len(EARLY_REPUBLIC_EVENTS)}个")
    print(f"南京十年: {len(NANJING_DECADE_EVENTS)}个")
    print(f"抗日战争: {len(SINO_JAPANESE_WAR_EVENTS)}个")
    print(f"解放战争: {len(CIVIL_WAR_EVENTS)}个")
    
    print("\n按影响力5级的重大事件：")
    major_events = [e for e in ALL_HISTORICAL_EVENTS if e.impact_level == 5]
    for event in major_events:
        print(f"- {event.date.strftime('%Y年%m月%d日')}: {event.title}")
