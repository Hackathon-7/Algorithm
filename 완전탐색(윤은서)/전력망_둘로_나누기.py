# 송전탑 개수를 세는 함수
def dfs(node, adj_list, visited):
    count = 1
    visited[node] = True
    for neighbor in adj_list[node]:
        if not visited[neighbor]:
            count += dfs(neighbor, adj_list, visited)
    return count

# 송전탑 연결 끊으면서 송전탑 개수 차이 최소값 반환
def solution(n, wires):
    adj_list = [[] for _ in range(n + 1)]
    # 인접 리스트 구성
    # v1에 v2를, v2에 v1을 (서로 연결되어 있음)
    for v1, v2 in wires:
        adj_list[v1].append(v2)
        adj_list[v2].append(v1)

    answer = float('inf')
    for v1, v2 in wires:
        # 전선을 끊음
        adj_list[v1].remove(v2)
        adj_list[v2].remove(v1)

        visited = [False] * (n + 1) #초기화
        
        # 각 전력망의 송전탑 개수 구함
        count1 = dfs(v1, adj_list, visited)
        count2 = dfs(v2, adj_list, visited)
        # 두 송전탑 개수의 차이
        difference = abs(count1 - count2)
        
        # 전에 계산한 것과 비교해서 더 작은값을 저장
        answer = min(answer, difference)

        # 다시 연결
        adj_list[v1].append(v2)
        adj_list[v2].append(v1)

    return answer
