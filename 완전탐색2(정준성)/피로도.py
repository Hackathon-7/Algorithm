answer = 0

def DFS(k, count, dungeons, check):
    global answer
    
    # answer 갱신
    answer = max(answer, count)

    for i in range(len(dungeons)):

        # 방문하지 않은 던전 and 현재 피로도가 해당 던전을 방문하기 위한 최소 피로도보다 크면
        if check[i] == 0 and k >= dungeons[i][0]:     
            check[i] = 1
            
            # k - 소모피로도, count+1, dungeons, [1, 0, 0, ...]
            DFS(k-dungeons[i][1], count+1, dungeons, check)
            check[i] = 0
    

def solution(k, dungeons):
    # answer = 0
    global answer
    check = [0]*len(dungeons)       # 방문 여부 체크하는 배열, [0, 0, 0, ...]
    
    # count: 탐험한 던전 개수, k: 남은 피로도
    DFS(k, 0, dungeons, check)     # 0: 방문한 던전의 개수를 0
    
    return answer