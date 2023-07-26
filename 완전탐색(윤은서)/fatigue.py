from itertools import permutations

def explore_dungeons(dungeons, current_fatigue, order):
    max_dungeons = 0
    count = 0

    for i in order:
        required_fatigue, consumed_fatigue = dungeons[i]
        if current_fatigue >= required_fatigue:
            count += 1
            current_fatigue -= consumed_fatigue

    return count

def solution(k, dungeons):
    n = len(dungeons)
    answer = 0

    # 가능한 모든 순열에 대해 탐험
    for order in permutations(range(n)):  
        answer = max(answer, explore_dungeons(dungeons, k, order))

    return answer
