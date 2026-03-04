from dataclasses import dataclass
from datetime import date
from typing import List, Optional

@dataclass
class CharacterEvent:
    """民国风云人物事件"""
    event_id: str
    date: date
    character_name: str
    title: str
    description: str
    character_role: str  # 政治家、军事家、革命家、文化名人、实业家
    significance: str
    related_people: List[str]
    historical_impact: int  # -100到100

# 民国重要人物关键事件
CHARACTER_EVENTS = [
    # 孙中山
    CharacterEvent(
        event_id="CHAR_001",
        date=date(1912, 1, 1),
        character_name="孙中山",
        title="孙中山就任临时大总统",
        description="1912年1月1日，孙中山在南京宣誓就任中华民国临时大总统，宣告中华民国成立，结束两千年帝制。孙中山提出'五权宪法'理念（行政、立法、司法、考试、监察），主张三民主义（民族、民权、民生）。就职演说强调'驱除鞑虏、恢复中华、建立民国、平均地权'。",
        character_role="革命家",
        significance="辛亥革命成功，共和制度建立，孙中山成为临时大总统，开启民国新纪元",
        related_people=["黄兴", "宋教仁", "袁世凯"],
        historical_impact=100
    ),
    
    CharacterEvent(
        event_id="CHAR_002",
        date=date(1925, 3, 12),
        character_name="孙中山",
        title="孙中山在北京逝世",
        description="孙中山患肝癌，在北京协和医院逝世，终年59岁。临终遗嘱：'革命尚未成功，同志仍需努力'，'和平、奋斗、救中国'。遗嘱由汪精卫笔录，宋庆龄、何香凝等在场见证。国民党、共产党、各界人士举行盛大公祭，北京30万人送葬。",
        character_role="革命家",
        significance="国父孙中山逝世，遗嘱'革命尚未成功'成为国民党精神遗产，国共两党均尊其为导师",
        related_people=["宋庆龄", "汪精卫", "蒋介石"],
        historical_impact=90
    ),
    
    # 袁世凯
    CharacterEvent(
        event_id="CHAR_003",
        date=date(1915, 12, 12),
        character_name="袁世凯",
        title="袁世凯称帝",
        description="袁世凯接受'劝进'，在北京宣布接受帝位，改国号为'中华帝国'，年号'洪宪'，定于1916年元旦登基。筹安会（杨度等六君子）鼓吹帝制，袁世凯自称符合'民意'。消息传出，全国哗然，蔡锷在云南起义讨袁，护国战争爆发。",
        character_role="政治家",
        significance="袁世凯复辟帝制，引发全国反对，护国战争爆发，民国共和制度受到严重威胁",
        related_people=["杨度", "蔡锷", "梁启超"],
        historical_impact=-80
    ),
    
    CharacterEvent(
        event_id="CHAR_004",
        date=date(1916, 6, 6),
        character_name="袁世凯",
        title="袁世凯忧郁病死",
        description="袁世凯在全国声讨、护国战争失败、众叛亲离中，于北京病死，终年57岁。称帝仅83天即被迫取消帝制，但已众叛亲离。临终前自悔：'他误我！'（指杨度等劝进者）临终仍不愿承认共和。死后葬于河南安阳，墓地简朴。",
        character_role="政治家",
        significance="窃国大盗袁世凯死亡，北洋军阀失去核心，中国进入军阀割据混战时代",
        related_people=["段祺瑞", "黎元洪"],
        historical_impact=-60
    ),
    
    # 蔡锷
    CharacterEvent(
        event_id="CHAR_005",
        date=date(1916, 11, 8),
        character_name="蔡锷",
        title="护国英雄蔡锷病逝",
        description="蔡锷在日本福冈医院病逝，年仅34岁。蔡锷因护国讨袁积劳成疾，喉癌恶化。遗嘱：'为四万万同胞惜'，'愿诸君勿忘共和'。灵柩运回国内，举国哀悼，国葬岳麓山。与小凤仙的传奇爱情（潜逃出北京）成为佳话。",
        character_role="军事家",
        significance="护国战争英雄蔡锷英年早逝，举国哀悼，其'再造共和'功绩被铭记",
        related_people=["小凤仙", "唐继尧", "梁启超"],
        historical_impact=75
    ),
    
    # 蒋介石
    CharacterEvent(
        event_id="CHAR_006",
        date=date(1927, 4, 18),
        character_name="蒋介石",
        title="蒋介石南京建立国民政府",
        description="蒋介石在南京成立国民政府，与武汉国民政府对峙（宁汉分裂）。此前4月12日，蒋介石在上海发动政变，大肆逮捕杀害共产党员和工人，史称'四一二反革命政变'。蒋介石自任国民政府主席和军事委员会主席，掌握党政军大权。",
        character_role="政治家",
        significance="蒋介石发动四一二政变，建立南京国民政府，国共合作破裂，中国进入十年内战",
        related_people=["汪精卫", "毛泽东", "周恩来"],
        historical_impact=-50
    ),
    
    CharacterEvent(
        event_id="CHAR_007",
        date=date(1936, 12, 12),
        character_name="蒋介石",
        title="西安事变：蒋介石被扣",
        description="张学良、杨虎城在西安扣留蒋介石，兵谏逼其停止内战、一致抗日，史称'西安事变'。蒋介石在华清池被扣，初拒绝停止剿共。周恩来代表中共赴西安谈判，宋美龄、宋子文斡旋。最终蒋介石口头承诺停止内战、联共抗日，12月25日获释。",
        character_role="政治家",
        significance="西安事变和平解决，蒋介石被迫停止内战，促成第二次国共合作，全民族抗战开始",
        related_people=["张学良", "杨虎城", "周恩来", "宋美龄"],
        historical_impact=85
    ),
    
    # 毛泽东
    CharacterEvent(
        event_id="CHAR_008",
        date=date(1935, 1, 15),
        character_name="毛泽东",
        title="遵义会议确立毛泽东领导地位",
        description="红军长征途中，在贵州遵义召开政治局扩大会议，批判博古、李德的军事错误，确立毛泽东在红军和中共的领导地位。会议决定由张闻天代替博古负总责，毛泽东进入政治局常委，实际掌握军事指挥权。此后红军在毛泽东指挥下四渡赤水、巧渡金沙江，摆脱围追堵截。",
        character_role="革命家",
        significance="遵义会议确立毛泽东领导地位，中共开始独立自主解决自身问题，红军转危为安",
        related_people=["周恩来", "张闻天", "博古", "朱德"],
        historical_impact=95
    ),
    
    CharacterEvent(
        event_id="CHAR_009",
        date=date(1945, 8, 28),
        character_name="毛泽东",
        title="毛泽东赴重庆谈判",
        description="抗战胜利后，毛泽东应蒋介石邀请，飞赴重庆谈判，震惊中外。此前外界认为毛泽东不敢去（担心被扣留），但毛泽东在周恩来陪同下赴重庆，展现共产党和平诚意。谈判43天，签订《双十协定》，但国共内战已不可避免。",
        character_role="革命家",
        significance="毛泽东赴重庆谈判展现政治勇气，签订双十协定，但国共内战仍无法避免",
        related_people=["蒋介石", "周恩来", "赫尔利"],
        historical_impact=70
    ),
    
    # 周恩来
    CharacterEvent(
        event_id="CHAR_010",
        date=date(1936, 12, 17),
        character_name="周恩来",
        title="周恩来西安谈判促成和平解决",
        description="西安事变后，周恩来受中共中央委派，飞赴西安与张学良、杨虎城会谈，并与蒋介石谈判。周恩来展现高超外交才能，说服张杨放弃'审判蒋介石'主张，劝说蒋介石停止内战、联共抗日。最终促成西安事变和平解决，避免内战扩大，推动全民族抗战。",
        character_role="政治家",
        significance="周恩来西安谈判促成事变和平解决，展现高超外交才能，促成第二次国共合作",
        related_people=["张学良", "杨虎城", "蒋介石"],
        historical_impact=80
    ),
    
    # 胡适
    CharacterEvent(
        event_id="CHAR_011",
        date=date(1917, 1, 1),
        character_name="胡适",
        title="胡适发表《文学改良刍议》",
        description="胡适在《新青年》发表《文学改良刍议》，提出文学改良'八不主义'：不作无病之呻吟、不摹仿古人、须讲求文法、不作无病呻吟、务去滥调套语、不用典、不讲对仗、不避俗字俗语。主张以白话文代替文言文，掀起白话文运动。",
        character_role="文化名人",
        significance="胡适白话文运动开启新文化运动，推动中国文学和思想的现代化转型",
        related_people=["陈独秀", "鲁迅", "蔡元培"],
        historical_impact=85
    ),
    
    # 鲁迅
    CharacterEvent(
        event_id="CHAR_012",
        date=date(1918, 5, 15),
        character_name="鲁迅",
        title="鲁迅发表《狂人日记》",
        description="鲁迅在《新青年》发表中国第一篇现代白话文小说《狂人日记》，以狂人视角控诉封建礼教'吃人'本质：'我翻开历史一查，这历史没有年代...每页上都写着仁义道德，我横竖睡不着，仔细看了半夜，才从字缝里看出字来，满本都写着两个字是吃人！'小说震撼文坛，开启现代文学新纪元。",
        character_role="文化名人",
        significance="鲁迅《狂人日记》开创中国现代文学，深刻批判封建礼教，影响深远",
        related_people=["胡适", "陈独秀", "钱玄同"],
        historical_impact=90
    ),
    
    CharacterEvent(
        event_id="CHAR_013",
        date=date(1936, 10, 19),
        character_name="鲁迅",
        title="鲁迅在上海逝世",
        description="鲁迅因肺结核在上海逝世，终年55岁。遗言：'不相信任何人的话，包括我的话'，'不宽恕我的敌人'。上海各界数万人参加追悼会，沈钧儒主持，宋庆龄敬献'民族魂'挽幛，毛泽东题词'鲁迅精神就是中华民族的精神'。棺材上覆盖红旗，墓碑刻'民族魂'三字。",
        character_role="文化名人",
        significance="民族魂鲁迅逝世，举国哀悼，其批判精神成为中华民族的精神遗产",
        related_people=["许广平", "宋庆龄", "毛泽东"],
        historical_impact=85
    ),
    
    # 张学良
    CharacterEvent(
        event_id="CHAR_014",
        date=date(1936, 12, 12),
        character_name="张学良",
        title="张学良发动西安事变",
        description="东北军将领张学良（时任西北剿共副司令）与西北军杨虎城，在西安扣留蒋介石，兵谏逼其停止内战、一致抗日。张学良九一八事变后失去东北（父亲张作霖被日本炸死），对'攘外必先安内'政策不满。事变提出八项主张：停止内战、释放政治犯、召开救国会议等。",
        character_role="军事家",
        significance="张学良发动西安事变，改变中国历史走向，促成国共合作抗日",
        related_people=["杨虎城", "蒋介石", "周恩来"],
        historical_impact=90
    ),
    
    CharacterEvent(
        event_id="CHAR_015",
        date=date(1936, 12, 25),
        character_name="张学良",
        title="张学良陪蒋介石回南京后被扣",
        description="西安事变和平解决后，张学良护送蒋介石飞回南京。抵达南京后，张学良立即被扣押，以'叛乱'罪名受军事审判，判处10年徒刑，随即被'特赦'，但长期软禁。这一软禁长达半个多世纪（1936-1990），直到蒋经国去世后才恢复自由。张学良后悔：'我做错了'。",
        character_role="军事家",
        significance="张学良被蒋介石软禁，失去自由50余年，成为西安事变最大牺牲者",
        related_people=["蒋介石", "赵四小姐"],
        historical_impact=-70
    ),
    
    # 宋庆龄
    CharacterEvent(
        event_id="CHAR_016",
        date=date(1927, 8, 1),
        character_name="宋庆龄",
        title="宋庆龄发表声明退出国民党",
        description="宋庆龄（孙中山遗孀）在汉口发表《为抗议违反孙中山的革命原则和政策的声明》，宣布退出国民党，严厉谴责蒋介石背叛革命、屠杀共产党员和工人。声明指出：'国民党已不再是革命的政党...孙先生的事业已被摧毁'。此后宋庆龄长期与中共合作，被誉为'国之瑰宝'。",
        character_role="政治家",
        significance="宋庆龄退出国民党谴责蒋介石，坚持孙中山革命路线，成为民主运动旗帜",
        related_people=["蒋介石", "孙中山", "宋美龄"],
        historical_impact=75
    ),
    
    # 宋美龄
    CharacterEvent(
        event_id="CHAR_017",
        date=date(1936, 12, 22),
        character_name="宋美龄",
        title="宋美龄飞赴西安营救蒋介石",
        description="西安事变后，宋美龄不顾安危，与宋子文飞赴西安营救蒋介石。她会见张学良、周恩来，斡旋各方，动之以情晓之以理。宋美龄对蒋介石耳语劝说（接受停止内战条件），对张学良保证其安全（事后未兑现），对周恩来展现合作诚意。在她推动下，西安事变和平解决。",
        character_role="政治家",
        significance="宋美龄西安斡旋展现政治才能和夫妻情深，促成事变和平解决",
        related_people=["蒋介石", "张学良", "周恩来", "宋子文"],
        historical_impact=70
    ),
]

def get_events_by_character(name: str) -> List[CharacterEvent]:
    """获取某个人物的所有事件"""
    return [e for e in CHARACTER_EVENTS if e.character_name == name]

def get_events_by_role(role: str) -> List[CharacterEvent]:
    """按角色类型筛选事件"""
    return [e for e in CHARACTER_EVENTS if e.character_role == role]

def get_events_by_period(start: date, end: date) -> List[CharacterEvent]:
    """按时间段筛选事件"""
    return [e for e in CHARACTER_EVENTS if start <= e.date <= end]

def get_related_network(name: str) -> dict:
    """获取人物关系网络"""
    events = get_events_by_character(name)
    related = set()
    for event in events:
        related.update(event.related_people)
    return {
        "中心人物": name,
        "直接关联": list(related),
        "重要事件数": len(events)
    }
