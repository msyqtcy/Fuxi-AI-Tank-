## 系统架构图

```mermaid
graph TD
    A[摄像头输入] -->|图像数据| B(MiMo-Vision Agent)
    C[MSPM0 单片机] -->|位置/状态| D(MiMo-Pro Agent)
    B -->|目标坐标| D
    D -->|控制指令| C

    style B fill:#f9f,stroke:#333,stroke-width:2px
    style D fill:#bbf,stroke:#333,stroke-width:2px