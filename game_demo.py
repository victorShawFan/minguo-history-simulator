#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
历史模拟器：民国 - 试玩演示版
可以体验历史事件、做出决策、影响历史走向
"""

import random
from datetime import date
from config import *
from historical_events_extended import ALL_HISTORICAL_EVENTS as HISTORICAL_EVENTS

class MinguoGame:
    def __init__(self):
        self.year = START_YEAR
        self.month = 1
        self.stats = INITIAL_STATS.copy()
        self.game_over = False
        self.events_triggered = []
        
    def display_header(self):
        print("\n" + "="*60)
        print("🏛️  历史模拟器：民国 (1912-1949)")
        print("="*60)
        
    def display_status(self):
        print(f"\n📅 当前时间：{self.year}年{self.month}月")
        print("\n📊 国力状态：")
        for key, value in self.stats.items():
            bar = "█" * (value // 5) + "░" * (20 - value // 5)
            print(f"  {key:8s}: [{bar}] {value}")
        print()
        
    def get_events_for_year(self):
        """获取当前年份的历史事件"""
        events = []
        for event in HISTORICAL_EVENTS:
            if event.date.year == self.year and event.event_id not in self.events_triggered:
                events.append(event)
        return events
    
    def trigger_event(self, event):
        """触发历史事件"""
        print("\n" + "🔔 " + "─"*56)
        print(f"📰 重大事件：{event.title}")
        print("─"*58)
        print(f"\n📖 {event.description}\n")
        print(f"🎯 影响力等级：{'⭐' * event.impact_level}")
        print(f"👥 关键人物：{', '.join(event.key_figures)}")
        print(f"📍 地点：{', '.join(event.locations)}")
        
        self.events_triggered.append(event.event_id)
        
        # 根据事件类型自动影响国力
        if "战争" in event.tags or "战役" in event.tags:
            change = random.randint(-15, -5)
            self.stats["经济"] = max(0, self.stats["经济"] + change)
            self.stats["民众支持"] = max(0, self.stats["民众支持"] + change)
            print(f"\n⚔️  战争影响：经济和民众支持 {change}")
        elif "改革" in event.tags or "新政" in event.tags:
            change = random.randint(5, 15)
            self.stats["威望"] = min(100, self.stats["威望"] + change)
            print(f"\n📈 改革红利：威望 +{change}")
        
    def make_decision(self):
        """玩家决策"""
        print("\n" + "💭 " + "─"*56)
        print("请选择您的应对策略：")
        print("─"*58)
        
        decisions = [
            ("1", "🎖️  加强军事力量", {"军事实力": 10, "经济": -5}),
            ("2", "💰 发展经济建设", {"经济": 12, "民众支持": 5}),
            ("3", "🤝 改善外交关系", {"外交关系": 10, "威望": 5}),
            ("4", "📚 推动教育文化", {"教育": 8, "文化": 8, "威望": 3}),
            ("5", "⏭️  维持现状（跳过）", {})
        ]
        
        for key, desc, _ in decisions:
            print(f"  {desc}")
            
        while True:
            choice = input("\n👉 请输入选项编号 (1-5): ").strip()
            if choice in ["1", "2", "3", "4", "5"]:
                break
            print("❌ 无效选项，请重新输入")
        
        # 应用决策效果
        _, desc, effects = decisions[int(choice)-1]
        if effects:
            print(f"\n✅ 您选择了：{desc}")
            print("📊 效果：")
            for stat, change in effects.items():
                self.stats[stat] = max(0, min(100, self.stats[stat] + change))
                sign = "+" if change > 0 else ""
                print(f"   {stat}: {sign}{change}")
        else:
            print("\n⏭️  您选择维持现状")
            
    def advance_time(self):
        """时间推进"""
        self.month += 3  # 每回合推进3个月
        if self.month > 12:
            self.year += 1
            self.month = 1
            
    def check_game_over(self):
        """检查游戏是否结束"""
        # 检查失败条件
        if self.stats["民众支持"] <= 10:
            print("\n💥 民心尽失！政权崩溃，游戏结束...")
            self.game_over = True
            return True
            
        if self.stats["经济"] <= 5:
            print("\n💥 经济崩溃！国家破产，游戏结束...")
            self.game_over = True
            return True
            
        # 检查时间结束
        if self.year >= END_YEAR:
            print(f"\n🎊 恭喜！您成功引导民国走过了{END_YEAR - START_YEAR}年历程！")
            self.game_over = True
            return True
            
        return False
    
    def play(self):
        """主游戏循环"""
        self.display_header()
        print("\n欢迎来到《历史模拟器：民国》！")
        print("您将扮演民国时期的决策者，面对历史的关键时刻...")
        print("通过您的选择，可能改写历史的进程！\n")
        
        input("按回车键开始游戏...")
        
        turn = 1
        while not self.game_over:
            print("\n" + "🎮 " + "="*56)
            print(f"第 {turn} 回合")
            print("="*58)
            
            self.display_status()
            
            # 触发当年的历史事件
            events = self.get_events_for_year()
            if events:
                # 随机选择一个事件
                event = random.choice(events)
                self.trigger_event(event)
                self.make_decision()
            else:
                print("\n📰 本回合风平浪静，没有重大事件发生")
                print("💡 提示：可以选择主动发展国力")
                self.make_decision()
            
            # 时间推进
            self.advance_time()
            
            # 检查游戏结束条件
            if self.check_game_over():
                break
                
            turn += 1
            
            # 每10回合询问是否继续
            if turn % 10 == 0:
                print("\n" + "─"*58)
                cont = input("继续游戏？(y/n): ").strip().lower()
                if cont != 'y':
                    print("\n👋 感谢试玩！游戏已保存退出")
                    break
        
        # 游戏结束，显示总结
        self.show_summary()
        
    def show_summary(self):
        """显示游戏总结"""
        print("\n" + "🏆 " + "="*56)
        print("游戏总结")
        print("="*58)
        print(f"\n⏱️  游戏时长：{self.year - START_YEAR}年（{START_YEAR}-{self.year}）")
        print(f"📝 触发事件：{len(self.events_triggered)}个")
        print("\n📊 最终国力：")
        total_score = sum(self.stats.values())
        for key, value in self.stats.items():
            print(f"  {key:8s}: {value}")
        print(f"\n🎯 综合评分：{total_score}/700")
        
        # 评级
        if total_score >= 600:
            rating = "SSS - 完美统治！"
        elif total_score >= 500:
            rating = "SS - 卓越领导！"
        elif total_score >= 400:
            rating = "S - 出色表现！"
        elif total_score >= 300:
            rating = "A - 良好发展"
        elif total_score >= 200:
            rating = "B - 勉强及格"
        else:
            rating = "C - 亟需改进"
            
        print(f"🏅 评级：{rating}\n")

if __name__ == "__main__":
    game = MinguoGame()
    try:
        game.play()
    except KeyboardInterrupt:
        print("\n\n👋 游戏已中断，感谢试玩！")
    except Exception as e:
        print(f"\n❌ 游戏出现错误：{e}")
