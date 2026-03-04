# 《历史模拟器：民国》

> 一款AI驱动的文字冒险策略游戏，让你穿越到1912年体验波澜壮阔的民国风云

## 🎮 游戏简介

《历史模拟器：民国》是一款基于大语言模型（LLM）驱动的文字冒险策略游戏。玩家将扮演民国时期的历史人物，在北洋军阀混战、国民革命、抗日战争等历史大背景下，通过自己的选择影响历史走向。

### 灵感来源
- Steam游戏：[历史模拟器系列](https://store.steampowered.com/app/4304230/_/?l=schinese)
- GLM-5驱动的《历史模拟器：崇祯》

### 技术特点
- 🤖 **AI驱动剧情**：使用GPT-5.1生成动态剧情和NPC对话
- 📜 **真实历史事件**：袁世凯称帝、五四运动、九一八事变等
- 🎭 **角色扮演**：多种职业背景（学者、商人、军人、革命者）
- 💾 **存档系统**：随时保存/加载游戏进度

## 🕰️ 游戏时间线

| 时期 | 年份 | 主要事件 |
|------|------|----------|
| 北洋时期 | 1912-1928 | 袁世凯称帝、护国运动、五四运动 |
| 南京十年 | 1928-1937 | 北伐战争、九一八事变、西安事变 |
| 抗日战争 | 1937-1945 | 七七事变、淞沪会战、重庆轰炸 |
| 解放战争 | 1945-1949 | 重庆谈判、三大战役、渡江战役 |

## 🎯 角色属性

| 属性 | 说明 |
|------|------|
| 💰 资产 | 金钱，用于投资、捐款、购买物资 |
| 📢 影响力 | 社会地位和声望 |
| ⚔️ 军事 | 军事能力和兵力 |
| 🧠 智力 | 学识和判断力 |
| 💬 魅力 | 人际交往能力 |
| ❤️ 健康 | 身体状况 |

## 🚀 快速开始

### 安装

```bash
git clone https://github.com/victorShawFan/minguo-history-simulator.git
cd minguo-history-simulator
```

### 运行

```bash
python game.py
```

### 游戏演示

```python
from game import MinguoGame

# 创建游戏
game = MinguoGame()
game.start()

# 创建角色
game.create_character("李明远", "scholar")
game.player.title = "北大教授"

# 查看状态
print(game.get_status())

# 生成事件
event = game.generate_random_event()
print(event['description'])

# 做出选择
result = game.process_choice(event['choices'][0])
print(f"影响: {result}")
```

## 📂 项目结构

```
minguo-history-simulator/
├── game.py              # 主游戏文件
├── README.md            # 项目说明
├── TODO.md              # 开发计划
├── ai_engine.py         # AI引擎模块（开发中）
├── events/              # 历史事件数据（计划）
│   ├── beiyang.json     # 北洋时期事件
│   ├── nanjing.json     # 南京十年事件
│   └── war.json         # 抗战时期事件
└── saves/               # 存档文件夹
```

## 🛠️ 开发计划

### v0.1 - 基础框架 ✅
- [x] 角色系统（属性、派系）
- [x] 游戏状态管理
- [x] 历史事件系统
- [x] 存档/读档功能
- [x] 基础UI界面

### v0.2 - AI集成（进行中）
- [ ] 接入GPT-5.1 API
- [ ] AI生成动态事件
- [ ] AI驱动NPC对话
- [ ] 智能剧情分支

### v0.3 - 内容扩充
- [ ] 更多历史事件（50+）
- [ ] 历史人物系统（蒋介石、毛泽东等）
- [ ] 地图系统（北京、上海、南京等）
- [ ] 关系网络系统

### v0.4 - 游戏平衡
- [ ] 属性平衡调整
- [ ] 难度系统
- [ ] 多结局设计
- [ ] 成就系统

### v1.0 - 完整版
- [ ] Web界面
- [ ] 多语言支持
- [ ] 音效和背景音乐
- [ ] 完整历史剧本

## 🤝 贡献指南

欢迎贡献代码、历史事件剧本、bug报告！

1. Fork 本仓库
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 开启 Pull Request

## 📜 历史参考资料

- 《民国史》
- 《北洋军阀统治时期史话》
- 《蒋介石日记》
- 百度百科、维基百科

## 📝 更新日志

### 2026-03-04
- 初始化项目
- 完成基础游戏框架
- 添加北洋时期、南京十年、抗战时期历史事件
- 实现角色创建和属性系统
- 实现存档/读档功能

## 📧 联系方式

- GitHub: [@victorShawFan](https://github.com/victorShawFan)
- 项目地址: https://github.com/victorShawFan/minguo-history-simulator

## 📄 开源协议

MIT License
