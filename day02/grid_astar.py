import heapq

grid = [

    [1,  1,  1,  3,  1],

    [1, -1, -1,  3,  1],

    [1, -1,  5,  3,  1],

    [1,  1,  1,  1,  1],

    [1,  1,  1,  1,  1],

]

start = (0, 0)

goal = (4, 4)

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]


# 휴리스틱 함수: 현재 위치에서 목표까지의 맨해튼 거리

def heuristic(a, b):

    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def grid_astar(grid, start, goal):

    rows = len(grid)

    cols = len(grid[0])

    # g_cost: 출발점에서 현재까지의 실제 비용 (Dijkstra의 distances와 동일)

    g_cost = [[float('inf')] * cols for _ in range(rows)]

    g_cost[start[0]][start[1]] = 0

    parent = [[None] * cols for _ in range(rows)]

    # 우선순위 큐: (f, 행, 열)

    # f = g + h  ← Dijkstra와의 차이점!

    heap = []

    h = heuristic(start, goal)           # 시작점에서 목표까지의 추정 거리

    heapq.heappush(heap, (0 + h, start[0], start[1]))

    visited = set()

    visit_count = 0    # 탐색한 칸 수를 세기

    while heap:

        f, r, c = heapq.heappop(heap)

        if (r, c) in visited:

            continue

        visited.add((r, c))

        visit_count += 1

        if (r, c) == goal:

            break

        for dr, dc in directions:

            nr, nc = r + dr, c + dc

            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] != -1:

                new_g = g_cost[r][c] + grid[nr][nc]

                if new_g < g_cost[nr][nc]:

                    g_cost[nr][nc] = new_g

                    h = heuristic((nr, nc), goal)   # 이웃에서 목표까지의 추정 거리

                    f = new_g + h               # f = g + h

                    parent[nr][nc] = (r, c)

                    heapq.heappush(heap, (f, nr, nc))

    # 경로 복원

    path = []

    current = goal

    while current is not None:

        path.append(current)

        current = parent[current[0]][current[1]]

    path.reverse()

    return g_cost[goal[0]][goal[1]], path, visit_count


# 실행

total_cost, path, count = grid_astar(grid, start, goal)

print(f"최소 비용: {total_cost}")

print(f"탐색한 칸 수: {count}")

print(f"경로: {path}")

# 격자 맵에 경로 표시

print("\n=== 경로 시각화 ===")

for r in range(len(grid)):

    row_str = ""

    for c in range(len(grid[0])):

        if (r, c) == start:

            row_str += " S "

        elif (r, c) == goal:

            row_str += " G "

        elif (r, c) in path:

            row_str += " * "

        elif grid[r][c] == -1:

            row_str += " ■ "

        else:

            row_str += f" {grid[r][c]} "

    print(row_str)
