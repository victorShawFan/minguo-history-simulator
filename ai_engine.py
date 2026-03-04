"""
AI引擎模块 - 使用GPT-5.1驱动游戏剧情生成

功能：
1. 动态事件生成
2. NPC对话生成
3. 历史背景描述
4. 玩家行为后果预测
"""

import json
import os
from typing import Dict, List, Optional
from dataclasses import dataclass


@dataclass
class EventContext:
    """事件上下文"""
    year: int
    month: int
    location: str
    era: str
    player_name: str
    player_faction: str
    player_attributes: Dict[str, int]


class AIEngine:
    """AI引擎 - 驱动游戏剧情"""
    
    def __init__(self, api_key: Optional[str] = None, model: str = "gpt-4"):
        """
        初始化AI引擎
        
        Args:
            api_key: OpenAI API Key
            model: 模型名称（gpt-4, gpt-3.5-turbo等）
        """
        self.api_key = api_key or os.getenv('OPENAI_API_KEY')
        self.model = model
        self.conversation_history = []
        
    def generate_event(self, context: EventContext) -> Dict:
        """
        生成动态历史事件
        
        Args:
            context: 游戏上下文
            
        Returns:
            事件字典，包含描述和选项
        """
        prompt = self._build_event_prompt(context)
        
        if not self.api_key:
            return self._fallback_event(context)
        
        try:
            response = self._call_gpt(prompt)
            event = self._parse_event_response(response)
            return event
        except Exception as e:
            print(f"AI生成失败，使用备用事件: {e}")
            return self._fallback_event(context)
    
    def generate_npc_dialogue(
        self,
        npc_name: str,
        npc_background: str,
        player_action: str,
        context: EventContext
    ) -> str:
        """
        生成NPC对话
        
        Args:
            npc_name: NPC名字
            npc_background: NPC背景
            player_action: 玩家行为
            context: 游戏上下文
            
        Returns:
            NPC回复文本
        """
        prompt = f"""
你是{npc_name}，{npc_background}。

当前时间：{context.year}年{context.month}月
地点：{context.location}
时代背景：{context.era}

{context.player_name}对你说：{player_action}

请以{npc_name}的身份，符合历史背景和人物性格地回复（100字以内）：
"""
        
        if not self.api_key:
            return f"{npc_name}：这是一个有趣的想法，让我考虑一下。"
        
        try:
            response = self._call_gpt(prompt, max_tokens=200)
            return response.strip()
        except Exception as e:
            print(f"对话生成失败: {e}")
            return f"{npc_name}：这是一个有趣的想法，让我考虑一下。"
    
    def analyze_choice_consequence(
        self,
        choice: str,
        context: EventContext
    ) -> Dict[str, int]:
        """
        分析玩家选择的后果
        
        Args:
            choice: 玩家选择
            context: 游戏上下文
            
        Returns:
            属性变化字典
        """
        prompt = f"""
游戏场景：
- 时间：{context.year}年{context.month}月
- 地点：{context.location}
- 玩家：{context.player_name}（{context.player_faction}）
- 当前属性：资产{context.player_attributes.get('money', 0)}，影响力{context.player_attributes.get('influence', 0)}

玩家选择：{choice}

请分析这个选择的后果，以JSON格式返回属性变化：
{{
  "money": -500,      # 资产变化（可正可负）
  "influence": 20,    # 影响力变化
  "military": 0,      # 军事力量变化
  "health": -5,       # 健康变化
  "reasoning": "简短说明原因"
}}
"""
        
        if not self.api_key:
            return {
                "money": -100,
                "influence": 10,
                "military": 0,
                "health": 0
            }
        
        try:
            response = self._call_gpt(prompt, max_tokens=150)
            consequence = json.loads(response)
            return consequence
        except Exception as e:
            print(f"后果分析失败: {e}")
            return {"money": -100, "influence": 10}
    
    def generate_historical_narration(
        self,
        event_name: str,
        context: EventContext
    ) -> str:
        """
        生成历史背景叙述
        
        Args:
            event_name: 事件名称
            context: 游戏上下文
            
        Returns:
            历史背景描述文本
        """
        prompt = f"""
以历史解说员的口吻，描述民国历史事件：{event_name}

时间：{context.year}年{context.month}月
地点：{context.location}

要求：
1. 200字左右
2. 符合历史事实
3. 生动形象，有画面感
4. 突出时代氛围
"""
        
        if not self.api_key:
            return f"{context.year}年，{event_name}爆发，中国历史进入新的篇章..."
        
        try:
            response = self._call_gpt(prompt, max_tokens=300)
            return response.strip()
        except Exception as e:
            print(f"叙述生成失败: {e}")
            return f"{context.year}年，{event_name}爆发，中国历史进入新的篇章..."
    
    def _build_event_prompt(self, context: EventContext) -> str:
        """构建事件生成提示"""
        return f"""
你是《历史模拟器：民国》的剧情生成器。

当前游戏状态：
- 时间：{context.year}年{context.month}月
- 时代：{context.era}
- 地点：{context.location}
- 玩家：{context.player_name}（{context.player_faction}）
- 玩家属性：
  * 资产：{context.player_attributes.get('money', 0)}银元
  * 影响力：{context.player_attributes.get('influence', 0)}
  * 军事：{context.player_attributes.get('military', 0)}
  * 智力：{context.player_attributes.get('intelligence', 0)}
  * 魅力：{context.player_attributes.get('charisma', 0)}

请生成一个符合历史背景、有趣且有选择性的事件，以JSON格式返回：

{{
  "name": "事件名称",
  "type": "political/economic/social/military",
  "description": "事件描述（100-150字）",
  "choices": [
    {{
      "text": "选项1",
      "effect": {{"money": -500, "influence": 20}},
      "reasoning": "简短说明后果"
    }},
    {{
      "text": "选项2",
      "effect": {{"military": 10, "health": -5}},
      "reasoning": "简短说明后果"
    }},
    {{
      "text": "选项3",
      "effect": {{"intelligence": 5}},
      "reasoning": "简短说明后果"
    }}
  ]
}}

要求：
1. 符合{context.year}年的历史背景
2. 与玩家当前派系和属性相关
3. 提供3个有意义的选择
4. 每个选择有不同的影响
"""
    
    def _call_gpt(self, prompt: str, max_tokens: int = 500) -> str:
        """
        调用GPT API
        
        Args:
            prompt: 提示文本
            max_tokens: 最大token数
            
        Returns:
            GPT返回的文本
        """
        try:
            import openai
            
            openai.api_key = self.api_key
            
            response = openai.ChatCompletion.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": "你是《历史模拟器：民国》的AI引擎，负责生成符合历史背景的游戏内容。"},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=max_tokens,
                temperature=0.8
            )
            
            return response.choices[0].message.content
            
        except ImportError:
            raise Exception("请安装openai库: pip install openai")
        except Exception as e:
            raise Exception(f"GPT调用失败: {e}")
    
    def _parse_event_response(self, response: str) -> Dict:
        """解析GPT返回的事件JSON"""
        try:
            response = response.strip()
            if response.startswith("```json"):
                response = response[7:]
            if response.endswith("```"):
                response = response[:-3]
            
            event = json.loads(response.strip())
            
            required_keys = ["name", "description", "choices"]
            if not all(key in event for key in required_keys):
                raise ValueError("事件格式不完整")
            
            return event
            
        except Exception as e:
            print(f"解析事件失败: {e}")
            raise
    
    def _fallback_event(self, context: EventContext) -> Dict:
        """备用事件（AI不可用时）"""
        events_by_era = {
            "北洋时期 (1912-1928)": [
                {
                    "name": "街头偶遇",
                    "type": "social",
                    "description": f"在{context.location}的街头，你偶遇了一位神秘人物，他似乎有重要消息要告诉你。",
                    "choices": [
                        {
                            "text": "上前攀谈",
                            "effect": {"intelligence": 5, "charisma": 3},
                            "reasoning": "可能获得有价值的信息"
                        },
                        {
                            "text": "保持距离",
                            "effect": {},
                            "reasoning": "谨慎行事，避免麻烦"
                        },
                        {
                            "text": "暗中跟踪",
                            "effect": {"intelligence": 8, "health": -3},
                            "reasoning": "冒险调查，可能发现秘密"
                        }
                    ]
                },
                {
                    "name": "商业机会",
                    "type": "economic",
                    "description": "有商人找到你，希望投资开设现代工厂，承诺可观的回报。",
                    "choices": [
                        {
                            "text": "投资1000银元",
                            "effect": {"money": -1000, "influence": 15},
                            "reasoning": "风险投资，可能获得长期回报"
                        },
                        {
                            "text": "投资500银元",
                            "effect": {"money": -500, "influence": 8},
                            "reasoning": "小额试水，降低风险"
                        },
                        {
                            "text": "拒绝投资",
                            "effect": {},
                            "reasoning": "保守策略，保护资产"
                        }
                    ]
                }
            ]
        }
        
        import random
        era_events = events_by_era.get(context.era, events_by_era["北洋时期 (1912-1928)"])
        return random.choice(era_events)


class HistoricalKnowledgeBase:
    """历史知识库"""
    
    FAMOUS_FIGURES = {
        "袁世凯": {
            "faction": "北洋系",
            "period": (1912, 1916),
            "description": "北洋军阀首领，曾任中华民国大总统",
            "personality": "野心勃勃、政治手腕高超"
        },
        "孙中山": {
            "faction": "国民党",
            "period": (1912, 1925),
            "description": "革命先行者，中华民国国父",
            "personality": "坚定理想主义者、民主倡导者"
        },
        "蒋介石": {
            "faction": "国民党",
            "period": (1926, 1949),
            "description": "国民革命军总司令，国民政府领导人",
            "personality": "军事强人、权力欲强"
        },
        "毛泽东": {
            "faction": "共产党",
            "period": (1921, 1949),
            "description": "中国共产党领导人",
            "personality": "战略思想家、革命家"
        },
        "鲁迅": {
            "faction": "无党派",
            "period": (1912, 1936),
            "description": "文学家、思想家",
            "personality": "犀利批判、关心民生"
        }
    }
    
    HISTORICAL_LOCATIONS = {
        "北京": {
            "importance": "政治中心",
            "features": ["故宫", "天安门", "北大", "协和医院"]
        },
        "上海": {
            "importance": "经济中心",
            "features": ["外滩", "租界", "十里洋场", "南京路"]
        },
        "南京": {
            "importance": "国民政府首都",
            "features": ["中山陵", "总统府", "夫子庙"]
        },
        "延安": {
            "importance": "革命根据地",
            "features": ["宝塔山", "杨家岭", "窑洞"]
        }
    }
    
    @classmethod
    def get_figure_info(cls, name: str) -> Optional[Dict]:
        """获取历史人物信息"""
        return cls.FAMOUS_FIGURES.get(name)
    
    @classmethod
    def get_location_info(cls, location: str) -> Optional[Dict]:
        """获取地点信息"""
        return cls.HISTORICAL_LOCATIONS.get(location)
    
    @classmethod
    def is_figure_active(cls, name: str, year: int) -> bool:
        """判断人物在某年是否活跃"""
        figure = cls.FAMOUS_FIGURES.get(name)
        if not figure:
            return False
        start, end = figure["period"]
        return start <= year <= end


if __name__ == "__main__":
    context = EventContext(
        year=1919,
        month=5,
        location="北京",
        era="北洋时期 (1912-1928)",
        player_name="李明远",
        player_faction="学者",
        player_attributes={
            "money": 1000,
            "influence": 100,
            "military": 0,
            "intelligence": 70,
            "charisma": 60
        }
    )
    
    engine = AIEngine()
    
    print("=== 测试事件生成 ===")
    event = engine.generate_event(context)
    print(f"\n事件：{event['name']}")
    print(f"描述：{event['description']}")
    print("\n选项：")
    for i, choice in enumerate(event['choices'], 1):
        print(f"{i}. {choice['text']}")
    
    print("\n=== 测试历史人物查询 ===")
    figure = HistoricalKnowledgeBase.get_figure_info("鲁迅")
    print(f"鲁迅：{figure['description']}")
    print(f"性格：{figure['personality']}")
