def solution(answers):
    # 수포자 1, 2, 3의 찍기 패턴
    pattern1 = [1, 2, 3, 4, 5]
    pattern2 = [2, 1, 2, 3, 2, 4, 2, 5]
    pattern3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    # 각 수포자가 맞춘 문제 수
    correct1 = 0
    correct2 = 0
    correct3 = 0
    
    for i in range(len(answers)):
        # 각 수포자의 답안 패턴을 순환하도록 인덱스 계산
        index1 = i % len(pattern1)
        index2 = i % len(pattern2)
        index3 = i % len(pattern3)
        
        # 정답과 비교하여 맞힌 문제 수 증가
        if answers[i] == pattern1[index1]:
            correct1 += 1
        if answers[i] == pattern2[index2]:
            correct2 += 1
        if answers[i] == pattern3[index3]:
            correct3 += 1
    
    # 가장 많은 문제를 맞힌 수포자 찾기
    max_correct = max(correct1, correct2, correct3)
    result = []
    if max_correct == correct1:
        result.append(1)
    if max_correct == correct2:
        result.append(2)
    if max_correct == correct3:
        result.append(3)
    
    return result
