# 오늘 수업 내용

| 용어 | 뜻 | Day 1과의 연결 |
|------|----|----------------|
| 가중치(Weight) | 간선(이동)에 붙는 비용. 거리, 시간, 위험도 등 | Day 1 BFS는 모든 가중치가 1이라고 가정 |
| 우선순위 큐(Priority Queue) | 비용이 가장 작은 것부터 꺼내는 큐 | Day 1 BFS의 일반 큐(FIFO)를 대체 |
| heapq | Python의 우선순위 큐 라이브러리 | Day 1의 deque를 대체 |
| Dijkstra | 가중치 그래프에서 최단 비용 경로를 찾는 알고리즘 | BFS + 우선순위 큐 + 비용 누적 |
| 휴리스틱(Heuristic) | 목표까지 남은 거리의 추정값 | Dijkstra에는 없고 A*에서 추가됨 |
| A* | Dijkstra + 휴리스틱. 목표 방향을 우선 탐색 | Dijkstra보다 탐색 범위가 좀 더 좁음 |
| g, h, f | g=출발~현재 비용, h=현재~목표 추정, f=g+h | g만 쓰면 Dijkstra, f를 쓰면 A* |
| global_planner | ROS에서 A*/Dijkstra로 전역 경로를 계획하는 컴포넌트 | costmap(장애물 지도) 위에서 동작 |