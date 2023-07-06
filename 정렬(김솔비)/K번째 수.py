def solution(array, commands):
    answer = []

    for t in range(len(commands)): # commands의 길이만큼 반복
        temp = array[commands[t][0]-1:commands[t][1]] 
        # i부터 j까지 슬라이싱하고 k번째 수 구하는 배열 받기
        temp.sort() # 정렬
        answer.append(temp[commands[t][2] - 1]) # k번째 숫자 구하기

    return answer
