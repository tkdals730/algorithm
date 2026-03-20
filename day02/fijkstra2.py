import heapq

# VisuAlgo에서 입력한 것과 동일한 그래프

# {노드: [(이웃, 비용), ...]} 형태

graph = {

    0: [(1, 1), (2, 4)],

    1: [(2, 2), (3, 5)],

    2: [(3, 1), (4, 3)],

    3: [(4, 2)],

    4: []

}


def dijkstra(graph, start):

    distances = {node: float('inf') for node in graph}

    distances[start] = 0

    heap = []

    heapq.heappush(heap, (0, start))

    visited = set()

    while heap:

        cost, node = heapq.heappop(heap)

        if node in visited:

            continue

        visited.add(node)

        print(f"  확정: 노드 {node}, 비용 {cost}")  # 디버그 출력

        for neighbor, weight in graph[node]:

            new_cost = cost + weight

            if new_cost < distances[neighbor]:

                distances[neighbor] = new_cost

                heapq.heappush(heap, (new_cost, neighbor))

                print(f"    → 노드 {neighbor} 업데이트: {new_cost}")  # 디버그 출력

    return distances


print("=== Dijkstra 실행 과정 ===")

result = dijkstra(graph, 0)

print()

print("=== 최종 결과 ===")

print(result)
