def solution(array, commands):
    # k번째 숫자 담아둘 배열
    answer = []

    # commands = [i, j, k] 배열
    for cmd in commands:
        # i, j, k 변수에 commands 배열에 있는 숫자 삽입
        i, j, k = cmd

        # i번째부터 j번째까지의 원하는 배열 획득
        want = array[i - 1:j]

        # 배열 정렬
        want.sort()

        # answer에 담기
        answer.append(want[k - 1])

    return answer


