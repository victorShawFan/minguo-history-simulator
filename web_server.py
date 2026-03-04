#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
历史模拟器：民国 - Web服务器
提供Web界面和API
"""

from flask import Flask, render_template, jsonify, request
from flask_cors import CORS
import random
from datetime import date
from config import *
from historical_events_extended import ALL_HISTORICAL_EVENTS as HISTORICAL_EVENTS

app = Flask(__name__)
CORS(app)

# 游戏会话存储（简单版，实际应该用数据库）
game_sessions = {}

class GameSession:
    def __init__(self, session_id):
        self.session_id = session_id
        self.year = START_YEAR
        self.month = 1
        self.stats = INITIAL_STATS.copy()
        self.events_triggered = []
        self.turn = 1
        self.game_over = False
        self.current_event = None
        
    def get_events_for_year(self):
        """获取当前年份的历史事件"""
        events = []
        for event in HISTORICAL_EVENTS:
            if event.date.year == self.year and event.event_id not in self.events_triggered:
                events.append(event)
        return events
    
    def trigger_random_event(self):
        """触发随机历史事件"""
        events = self.get_events_for_year()
        if events:
            event = random.choice(events)
            self.current_event = {
                'title': event.title,
                'description': event.description,
                'impact_level': event.impact_level,
                'key_figures': event.key_figures,
                'locations': event.locations,
                'tags': event.tags
            }
            self.events_triggered.append(event.event_id)
            
            # 自动影响
            if "战争" in event.tags or "战役" in event.tags:
                change = random.randint(-15, -5)
                self.stats["经济"] = max(0, self.stats["经济"] + change)
                self.stats["民众支持"] = max(0, self.stats["民众支持"] + change)
                self.current_event['auto_effect'] = f"战争影响：经济和民众支持 {change}"
            elif "改革" in event.tags or "新政" in event.tags:
                change = random.randint(5, 15)
                self.stats["威望"] = min(100, self.stats["威望"] + change)
                self.current_event['auto_effect'] = f"改革红利：威望 +{change}"
        else:
            self.current_event = None
            
    def make_decision(self, choice):
        """处理玩家决策"""
        decisions = {
            '1': {"name": "加强军事力量", "effects": {"军事实力": 10, "经济": -5}},
            '2': {"name": "发展经济建设", "effects": {"经济": 12, "民众支持": 5}},
            '3': {"name": "改善外交关系", "effects": {"外交关系": 10, "威望": 5}},
            '4': {"name": "推动教育文化", "effects": {"教育": 8, "文化": 8, "威望": 3}},
            '5': {"name": "维持现状", "effects": {}}
        }
        
        decision = decisions.get(choice, decisions['5'])
        effects = decision['effects']
        
        for stat, change in effects.items():
            self.stats[stat] = max(0, min(100, self.stats[stat] + change))
            
        return decision
    
    def advance_time(self):
        """时间推进"""
        self.month += 3
        if self.month > 12:
            self.year += 1
            self.month = 1
        self.turn += 1
        
    def check_game_over(self):
        """检查游戏结束"""
        if self.stats["民众支持"] <= 10:
            self.game_over = True
            return {"over": True, "reason": "民心尽失", "message": "民心尽失！政权崩溃"}
        if self.stats["经济"] <= 5:
            self.game_over = True
            return {"over": True, "reason": "经济崩溃", "message": "经济崩溃！国家破产"}
        if self.year >= END_YEAR:
            self.game_over = True
            return {"over": True, "reason": "胜利", "message": f"恭喜！成功引导民国走过{END_YEAR - START_YEAR}年！"}
        return {"over": False}
    
    def get_state(self):
        """获取当前游戏状态"""
        return {
            'year': self.year,
            'month': self.month,
            'turn': self.turn,
            'stats': self.stats,
            'current_event': self.current_event,
            'events_count': len(self.events_triggered),
            'game_over': self.game_over
        }

@app.route('/')
def index():
    """首页"""
    return render_template('game.html')

@app.route('/api/start', methods=['POST'])
def start_game():
    """开始新游戏"""
    session_id = str(random.randint(10000, 99999))
    game = GameSession(session_id)
    game_sessions[session_id] = game
    
    game.trigger_random_event()
    
    return jsonify({
        'session_id': session_id,
        'state': game.get_state()
    })

@app.route('/api/decision', methods=['POST'])
def make_decision():
    """做出决策"""
    data = request.json
    session_id = data.get('session_id')
    choice = data.get('choice')
    
    game = game_sessions.get(session_id)
    if not game:
        return jsonify({'error': '游戏会话不存在'}), 404
    
    # 应用决策
    decision = game.make_decision(choice)
    
    # 推进时间
    game.advance_time()
    
    # 检查游戏结束
    game_over_info = game.check_game_over()
    
    if not game_over_info['over']:
        # 触发新事件
        game.trigger_random_event()
    
    return jsonify({
        'decision': decision,
        'state': game.get_state(),
        'game_over': game_over_info
    })

@app.route('/api/state/<session_id>')
def get_state(session_id):
    """获取游戏状态"""
    game = game_sessions.get(session_id)
    if not game:
        return jsonify({'error': '游戏会话不存在'}), 404
    
    return jsonify({'state': game.get_state()})

if __name__ == '__main__':
    print("\n🚀 启动《历史模拟器：民国》Web服务器...")
    print("🌐 访问地址：http://localhost:5000")
    print("📱 在浏览器中打开即可开始游戏！\n")
    app.run(debug=True, port=5000, host='0.0.0.0')
