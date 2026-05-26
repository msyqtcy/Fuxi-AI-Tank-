# -*- coding: utf-8 -*-
import json
import time

# 模拟从摄像头获取的画面描述（实际会用 MiMo-Vision 分析图片）
mock_vision_input = "画面描述：前方1米处有一个红色的圆形靶心，背景是白色墙壁。"

# 模拟从单片机传来的状态（实际会通过串口读取）
mock_mcu_status = {"car_x": 0, "car_y": 0, "laser_status": "off", "battery": 85}

def mimo_reasoning_prompt(vision, status):
    prompt = f"""
    你是一个智能坦克的指挥官。
    【当前环境】{vision}
    【当前状态】位置({status['car_x']}, {status['car_y']})，电量{status['battery']}%
    
    任务：决定下一步动作。
    可选动作：FORWARD, TURN_LEFT, TURN_RIGHT, SHOOT, STOP
    
    请只输出一个动作，不要解释。
    """
    return prompt

if __name__ == "__main__":
    print("=== 模拟 AI Agent 决策过程 ===")
    print("1. 视觉感知：", mock_vision_input)
    print("2. 状态读取：", mock_mcu_status)
    
    action_prompt = mimo_reasoning_prompt(mock_vision_input, mock_mcu_status)
    print("\n3. 发送给 MiMo 的指令：")
    print(action_prompt)
    
    # 模拟 MiMo 的返回（实际是 API 返回）
    simulated_response = "TURN_RIGHT"
    print("\n4. MiMo 决策结果：", simulated_response)
    print("5. 正在发送指令给 MSPM0 单片机...")