def solution(answers):
    supoza1 = [1, 2, 3, 4, 5]
    supoza2 = [2, 1, 2, 3, 2, 4, 2, 5]
    supoza3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    scores = [0, 0, 0]  # 수포자 1, 2, 3의 점수를 저장할 리스트

    for idx, answer in enumerate(answers):
        # 수포자 1이 찍는 방식 반복, 값이 같으면 점수+1
        if answer == supoza1[idx % len(supoza1)]:
            scores[0] += 1
        if answer == supoza2[idx % len(supoza2)]:
            scores[1] += 1
        if answer == supoza3[idx % len(supoza3)]:
            scores[2] += 1

    max_score = max(scores)
    winners = [i + 1 for i, score in enumerate(scores) if score == max_score]

    return winners
