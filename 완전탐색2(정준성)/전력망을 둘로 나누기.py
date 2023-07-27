def build_graph(n, wires):
    # 그래프 구성을 위한 딕셔너리 초기화
    graph = {i: [] for i in range(1, n + 1)}

    # 전선 정보를 바탕으로 그래프 구성
    for wire in wires:
        a, b = wire
        graph[a].append(b)
        graph[b].append(a)

    return graph

def dfs_count(node, graph, visited):
    # DFS를 통해 서브 트리의 송전탑 개수를 구하는 함수
    count = 1
    visited[node] = True

    for neighbor in graph[node]:
        if not visited[neighbor]:
            count += dfs_count(neighbor, graph, visited)

    return count

def solution(n, wires):
    graph = build_graph(n, wires)
    min_diff = float('inf')  # 초기값을 무한대로 설정

    for wire in wires:
        a, b = wire
        # 전선을 끊었을 때의 서브 트리 크기 계산을 위해 방문 정보 초기화
        visited = {i: False for i in range(1, n + 1)}
        graph[a].remove(b)
        graph[b].remove(a)

        # 두 서브 트리의 송전탑 개수 계산
        count_a = dfs_count(a, graph, visited)
        count_b = dfs_count(b, graph, visited)

        # 두 서브 트리의 송전탑 개수 차이 계산
        diff = abs(count_a - count_b)

        # 최소 차이 값 갱신
        min_diff = min(min_diff, diff)

        # 그래프 원상 복구
        graph[a].append(b)
        graph[b].append(a)

    return min_diff
