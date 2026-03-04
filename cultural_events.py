# 历史模拟器：民国 - 文化与思想运动事件库
"""
涵盖新文化运动、白话文运动、文学革命等思想文化领域重大事件
数据来源：百科、今日头条《新青年与新文化运动》、《白话文运动》等
"""

from typing import List
from dataclasses import dataclass
from datetime import date

@dataclass
class CulturalEvent:
    """文化事件数据结构"""
    event_id: str
    title: str
    date: date
    description: str
    key_figures: List[str]
    publications: List[str]  # 相关刊物/作品
    impact: str
    tags: List[str]

# 新文化运动相关事件
NEW_CULTURE_MOVEMENT_EVENTS = [
    CulturalEvent(
        event_id="culture_1915_001",
        title="《新青年》杂志创刊",
        date=date(1915, 9, 15),
        description="陈独秀在上海创办《青年杂志》（后改名《新青年》），标志着新文化运动的开端。杂志以'民主'和'科学'为旗帜，猛烈抨击封建礼教，传播西方民主思想。",
        key_figures=["陈独秀", "李大钊", "胡适", "鲁迅"],
        publications=["新青年"],
        impact="成为新文化运动的主要思想阵地，集结了中国最优秀的知识分子，推动了思想启蒙。",
        tags=["新文化运动", "启蒙思想", "民主科学"]
    ),
    CulturalEvent(
        event_id="culture_1917_001",
        title="胡适发表《文学改良刍议》",
        date=date(1917, 1, 1),
        description="胡适在《新青年》上发表《文学改良刍议》，提出'八不主义'：不作言之无物的文字、不摹仿古人、须讲求文法、不作无病之呻吟、务去滥调套语、不用典、不讲对仗、不避俗字俗语。这标志着文学革命的正式开始。",
        key_figures=["胡适", "陈独秀"],
        publications=["新青年"],
        impact="揭开了白话文运动的序幕，动摇了文言文的统治地位。",
        tags=["文学革命", "白话文", "八不主义"]
    ),
    CulturalEvent(
        event_id="culture_1917_002",
        title="陈独秀发表《文学革命论》",
        date=date(1917, 2, 1),
        description="陈独秀发表《文学革命论》响应胡适，明确提出'推倒雕琢的阿谀的贵族文学，建设平易的抒情的国民文学；推倒陈腐的铺张的古典文学，建设新鲜的立诚的写实文学；推倒迂晦的艰涩的山林文学，建设明了的通俗的社会文学'。",
        key_figures=["陈独秀", "胡适"],
        publications=["新青年"],
        impact="将文学革命从'改良'推向'革命'，态度更加激进和彻底。",
        tags=["文学革命", "三大主义"]
    ),
    CulturalEvent(
        event_id="culture_1918_001",
        title="鲁迅发表《狂人日记》",
        date=date(1918, 5, 15),
        description="鲁迅在《新青年》第4卷第5号发表中国第一篇现代白话文小说《狂人日记》，以'疯子'的视角揭露封建礼教'吃人'的本质，喊出'救救孩子'的呼声。这是中国现代文学史上的里程碑。",
        key_figures=["鲁迅"],
        publications=["新青年", "狂人日记"],
        impact="标志着中国新文学的诞生，白话文从此成为文学创作的主流语言。",
        tags=["白话文小说", "鲁迅", "反封建"]
    ),
    CulturalEvent(
        event_id="culture_1918_002",
        title="鲁迅发表《孔乙己》",
        date=date(1918, 4, 1),
        description="鲁迅发表短篇小说《孔乙己》，通过描写一个穷困潦倒的读书人，深刻揭露了科举制度对知识分子的毒害和封建社会的冷酷。",
        key_figures=["鲁迅"],
        publications=["新青年", "孔乙己"],
        impact="成为中国现代文学经典，展现了鲁迅'哀其不幸，怒其不争'的人文关怀。",
        tags=["批判现实主义", "反封建"]
    ),
    CulturalEvent(
        event_id="culture_1918_003",
        title="李大钊发表《庶民的胜利》",
        date=date(1918, 11, 15),
        description="李大钊在《新青年》发表《庶民的胜利》和《Bolshevism的胜利》，热情欢呼俄国十月革命的胜利，率先在中国举起马克思主义的旗帜，预言'试看将来的环球，必是赤旗的世界'。",
        key_figures=["李大钊"],
        publications=["新青年"],
        impact="开启了马克思主义在中国的传播，为中国共产党的诞生奠定了思想基础。",
        tags=["马克思主义", "十月革命", "李大钊"]
    ),
    CulturalEvent(
        event_id="culture_1919_001",
        title="《新青年》出版马克思主义研究专号",
        date=date(1919, 5, 1),
        description="《新青年》第6卷第5号出版'马克思主义研究'专号，刊登李大钊的《我的马克思主义观》等文章，系统介绍马克思主义的基本原理。这是中国第一次大规模宣传马克思主义。",
        key_figures=["李大钊", "陈独秀"],
        publications=["新青年"],
        impact="推动马克思主义在中国的传播，为建党准备了理论基础。",
        tags=["马克思主义", "理论传播"]
    ),
    CulturalEvent(
        event_id="culture_1919_002",
        title="问题与主义之争",
        date=date(1919, 7, 20),
        description="胡适发表《多研究些问题，少谈些主义》，主张'改良主义'。李大钊撰文反驳，强调必须用马克思主义指导中国革命。这场论战反映了新文化运动阵营内部的分化。",
        key_figures=["胡适", "李大钊"],
        publications=["新青年", "每周评论"],
        impact="标志着新文化运动阵营的分裂，李大钊坚定选择了马克思主义道路。",
        tags=["思想论战", "改良与革命"]
    ),
    CulturalEvent(
        event_id="culture_1920_001",
        title="《新青年》改组为中共理论刊物",
        date=date(1920, 9, 1),
        description="《新青年》第8卷第1号起成为上海共产主义小组的机关刊物，公开宣传马克思主义和共产主义，标志着新文化运动的激进派与改良派彻底分道扬镳。",
        key_figures=["陈独秀", "李大钊"],
        publications=["新青年"],
        impact="《新青年》从文化启蒙刊物转变为政治革命刊物，新文化运动进入新阶段。",
        tags=["共产主义", "政治转向"]
    ),
]

# 文学作品与创作事件
LITERATURE_EVENTS = [
    CulturalEvent(
        event_id="literature_1921_001",
        title="文学研究会成立",
        date=date(1921, 1, 4),
        description="郑振铎、沈雁冰（茅盾）、叶绍钧（叶圣陶）等12人在北京发起成立文学研究会，主张'为人生'的现实主义文学，反对'为艺术而艺术'。创办《小说月报》作为会刊。",
        key_figures=["郑振铎", "茅盾", "叶圣陶", "朱自清"],
        publications=["小说月报"],
        impact="形成了中国现代文学史上第一个影响深远的文学流派，奠定了现实主义文学传统。",
        tags=["文学社团", "现实主义", "为人生"]
    ),
    CulturalEvent(
        event_id="literature_1921_002",
        title="创造社成立",
        date=date(1921, 7, 1),
        description="郭沫若、郁达夫、成仿吾等留日学生在东京成立创造社，倡导'为艺术而艺术'，强调个性解放和自我表现，形成浪漫主义文学流派。",
        key_figures=["郭沫若", "郁达夫", "成仿吾"],
        publications=["创造季刊", "创造周报"],
        impact="与文学研究会形成'双峰对峙'格局，丰富了中国现代文学的创作风格。",
        tags=["文学社团", "浪漫主义", "个性解放"]
    ),
    CulturalEvent(
        event_id="literature_1923_001",
        title="鲁迅出版《呐喊》",
        date=date(1923, 8, 1),
        description="鲁迅的第一部白话小说集《呐喊》由新潮社出版，收录《狂人日记》《孔乙己》《药》《阿Q正传》等14篇作品，成为中国现代文学的经典。",
        key_figures=["鲁迅"],
        publications=["呐喊"],
        impact="确立了鲁迅在中国现代文学史上的地位，奠定了批判现实主义传统。",
        tags=["鲁迅作品", "批判现实主义"]
    ),
    CulturalEvent(
        event_id="literature_1926_001",
        title="鲁迅出版《彷徨》",
        date=date(1926, 8, 1),
        description="鲁迅的第二部小说集《彷徨》出版，收录《祝福》《在酒楼上》《伤逝》等11篇作品，继续揭露封建社会的黑暗，关注底层人民的苦难。",
        key_figures=["鲁迅"],
        publications=["彷徨"],
        impact="深化了对中国社会的批判，艺术手法更加成熟。",
        tags=["鲁迅作品", "社会批判"]
    ),
    CulturalEvent(
        event_id="literature_1928_001",
        title="茅盾发表《子夜》",
        date=date(1933, 1, 1),
        description="茅盾的长篇小说《子夜》（实际1933年出版，但反映1920年代末的上海），描写民族资本家吴荪甫在帝国主义和官僚买办势力夹击下破产的故事，被誉为'中国第一部成功的现实主义长篇巨著'。",
        key_figures=["茅盾"],
        publications=["子夜"],
        impact="标志着中国现实主义文学创作的新高峰，深刻揭示了旧中国的社会矛盾。",
        tags=["茅盾", "现实主义长篇"]
    ),
]

# 教育与学术事件
EDUCATION_EVENTS = [
    CulturalEvent(
        event_id="education_1917_001",
        title="蔡元培出任北大校长",
        date=date(1917, 1, 4),
        description="蔡元培就任北京大学校长，实行'思想自由，兼容并包'的办学方针，聘请陈独秀、李大钊、胡适等新派人物任教，将北大改造为新文化运动的中心。",
        key_figures=["蔡元培", "陈独秀", "李大钊", "胡适"],
        publications=[],
        impact="北京大学成为新思想的策源地，为五四运动和新文化运动提供了重要阵地。",
        tags=["高等教育", "思想自由", "北京大学"]
    ),
    CulturalEvent(
        event_id="education_1918_001",
        title="北大成立马克思学说研究会",
        date=date(1920, 3, 1),
        description="李大钊在北京大学发起成立马克思学说研究会，这是中国最早系统研究马克思主义的学术团体。邓中夏、高君宇、毛泽东等都曾参加。",
        key_figures=["李大钊", "邓中夏", "高君宇"],
        publications=["马克思主义研究资料"],
        impact="培养了一批马克思主义信仰者，为建党准备了干部基础。",
        tags=["马克思主义", "学术研究"]
    ),
    CulturalEvent(
        event_id="education_1922_001",
        title="全国教育会议与学制改革",
        date=date(1922, 11, 1),
        description="北洋政府召开全国教育会议，通过'壬戌学制'（仿照美国六三三学制：小学6年，初中3年，高中3年），取代清末的'癸卯学制'。这是中国现代教育制度的重要改革。",
        key_figures=["蔡元培", "胡适"],
        publications=[],
        impact="确立了中国现代学制的基本框架，影响深远。",
        tags=["教育改革", "学制变革"]
    ),
]

# 白话文与语言文字改革
LANGUAGE_REFORM_EVENTS = [
    CulturalEvent(
        event_id="language_1920_001",
        title="国语统一筹备会成立",
        date=date(1913, 2, 15),
        description="北洋政府教育部成立'读音统一会'（后改名'国语统一筹备会'），开始制定国音标准和推广国语（即普通话的前身）。",
        key_figures=["吴稚晖", "钱玄同", "黎锦熙"],
        publications=[],
        impact="推动了汉语标准化进程，为全国语言统一奠定了基础。",
        tags=["语言改革", "国语运动"]
    ),
    CulturalEvent(
        event_id="language_1920_002",
        title="教育部规定小学课本改用白话文",
        date=date(1920, 1, 12),
        description="北洋政府教育部发布命令，规定从1920年秋季起，小学一、二年级的国文教科书改用白话文编写。这是白话文运动的重大胜利，标志着白话文取得了官方地位。",
        key_figures=["蔡元培", "胡适"],
        publications=[],
        impact="白话文从知识分子的实验走向全社会普及，彻底改变了中国的语言文字生态。",
        tags=["白话文", "教育改革", "语文教育"]
    ),
    CulturalEvent(
        event_id="language_1928_001",
        title="国语罗马字拼音方案公布",
        date=date(1928, 9, 26),
        description="国民政府大学院公布《国语罗马字拼音法式》，这是中国第一套由政府颁布的拉丁化拼音方案，用于注音和推广国语。",
        key_figures=["赵元任", "林语堂"],
        publications=[],
        impact="推动了汉语拼音化的探索，为后来的汉语拼音方案奠定了基础。",
        tags=["拼音方案", "语文现代化"]
    ),
]

# 合并所有文化事件
ALL_CULTURAL_EVENTS = (
    NEW_CULTURE_MOVEMENT_EVENTS +
    LITERATURE_EVENTS +
    EDUCATION_EVENTS +
    LANGUAGE_REFORM_EVENTS
)

def get_events_by_date_range(start_date: date, end_date: date) -> List[CulturalEvent]:
    """根据时间范围获取事件"""
    return [e for e in ALL_CULTURAL_EVENTS if start_date <= e.date <= end_date]

def get_events_by_figure(figure_name: str) -> List[CulturalEvent]:
    """根据历史人物获取相关文化事件"""
    return [e for e in ALL_CULTURAL_EVENTS if figure_name in e.key_figures]

def get_events_by_publication(pub_name: str) -> List[CulturalEvent]:
    """根据刊物/作品获取相关事件"""
    return [e for e in ALL_CULTURAL_EVENTS if pub_name in e.publications]

def search_cultural_events(keyword: str) -> List[CulturalEvent]:
    """关键词搜索文化事件"""
    results = []
    keyword_lower = keyword.lower()
    for event in ALL_CULTURAL_EVENTS:
        if (keyword_lower in event.title.lower() or
            keyword_lower in event.description.lower() or
            any(keyword_lower in tag.lower() for tag in event.tags)):
            results.append(event)
    return results

if __name__ == "__main__":
    print(f"文化事件库加载完成，共{len(ALL_CULTURAL_EVENTS)}个事件")
    print(f"新文化运动: {len(NEW_CULTURE_MOVEMENT_EVENTS)}个")
    print(f"文学创作: {len(LITERATURE_EVENTS)}个")
    print(f"教育改革: {len(EDUCATION_EVENTS)}个")
    print(f"语言文字改革: {len(LANGUAGE_REFORM_EVENTS)}个")
    
    print("\n新文化运动重要人物事件：")
    lu_xun_events = get_events_by_figure("鲁迅")
    for event in lu_xun_events:
        print(f"- {event.date.strftime('%Y年%m月%d日')}: {event.title}")
