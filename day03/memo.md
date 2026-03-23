# 오늘 주제
DWA (Dynamic Window Approach)
# 오늘 배운 용어
| 용어 | 뜻 | 이전 수업과의 연결 |
|------|----|----------------|
| Local Planner | 로봇 주변 환경을 보고 실시간으로 속도 명령을 생성하는 컴포넌트 | Day 2의 global planner와 짝 |
| DWA | Dynamic Window Approach. 로봇이 낼 수 있는 속도 범위 안에서 최적의 속도를 선택 | local_planner의 기본 알고리즘 |
| Costmap | 격자 맵의 각 칸에 비용(0~254)을 부여한 지도 | Day 1 격자 맵 + Day 2 가중치 개념의 실제 적용 |
| Static Layer | 저장된 지도 기반의 고정 장애물 레이어 | gmapping으로 만든 지도 (ROS 맵) |
| Obstacle Layer | LiDAR 등 센서로 감지한 실시간 장애물 레이어 | Day 1 BFS의 벽(1)과 유사하나 실시간 갱신 |
| Inflation Layer | 장애물 주변에 비용 그라디언트를 추가하는 레이어 | Day 2 Dijkstra의 비용 차이를 활용 |
| Velocity Space | (선속도, 각속도) 조합으로 이루는 2D 공간 | DWA가 이 공간에서 최적 속도를 탐색 |
| cmd_vel | 로봇에 보내는 속도 명령 토픽 | local_planner의 출력 |