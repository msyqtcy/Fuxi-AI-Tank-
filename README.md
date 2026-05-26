# Fuxi-AI-Tank-
A Vision-Based Autonomous Aiming System powered by Xiaomi MiMo V2.5 and Multi-Agent Collaboration. 
# 🚀 基于 Xiaomi MiMo 的视觉自主对抗智能车系统 (Fuxi-V1)
**"Live Demo Concept"**
https://www.bilibili.com/video/BV1uhVN6eETK/
**🏆 项目背景**  
本项目基于 2025 年全国大学生电子设计竞赛 E 题（简易自行瞄准装置）进行深度升级。利用 **Xiaomi MiMo-V2.5** 的多模态（Vision）与强推理（Pro）能力，将传统的“固定循迹”小车进化为“全向视觉感知 + 自主博弈决策”的智能体。

**🤖 系统架构**
我们构建了一个 **三层 Multi-Agent 协同架构**，实现了从感知到决策的闭环。

| 模块 | 技术栈 | 核心功能 |
| :--- | :--- | :--- |
| **👁️ 视觉感知 Agent** | MiMo-V2.5-Vision + OpenCV | 识别动态靶心、环境 SLAM、障碍物检测 |
| **🧠 决策规划 Agent** | MiMo-V2.5-Pro + LangChain | 实时生成运动策略、计算弹道提前量、博弈逻辑 |
| **✋ 运动控制 (MSPM0)** | TI MSPM0 (C语言) | 底层电机 PID、云台控制、激光发射 |

**📊 为什么选择 Xiaomi MiMo?**
*   **超长上下文 (1M Token)**: 用于记录全场对战历史，实现“越打越聪明”的策略调整。
*   **多模态能力**: 直接输入摄像头画面，无需复杂的传统 CV 算法即可识别靶纸状态。
*   **高并发推理**: 支撑每秒 10+ 次的决策循环。

**📸 硬件原型**
*<img width="1280" height="2284" alt="微信图片_20260526210340_1861_40" src="https://github.com/user-attachments/assets/15422839-87c6-47c3-bc76-6feeba354c10" />

*
> *注：保留了电赛 E 题的 MSPM0 底层硬件，上层接入 AI 算力，完美契合“软硬结合”理念。*

**📈 预期 Token 消耗**
预计在高强度测试下，单日 Token 消耗将超过 **8,000,000**，主要用于视觉推理与长文本策略生成。
