# enquene : 뒤에 데이터를 추가
# dequene : 앞의 데이터를 꺼냄

"""
활용 예시
- 프린터 출력 대기열
- ROS 토픽 베시지 버퍼
- BFS
"""

from collections import deque

queue = deque() # 이 친구는 뭐지
queue.append('A')
queue.append('B')
queue.append('C')
print(queue)
print(queue.popleft())
print(queue.popleft())
print(queue)