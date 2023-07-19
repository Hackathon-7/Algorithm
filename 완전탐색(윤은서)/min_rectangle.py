def solution(sizes):
    min_width = 0
    min_height = 0

    for width, height in sizes:
        # 가로와 세로 길이 중에서 더 큰 값을 최대 가로 길이로 설정
        max_side = max(width, height)
        # 가로와 세로 길이 중에서 더 작은 값을 최대 세로 길이로 설정
        min_side = min(width, height)

        # 현재 명함의 최대 가로 길이가 이전에 계산한 최대 가로 길이보다 크면 업데이트
        if max_side > min_width:
            min_width = max_side

        # 현재 명함의 최대 세로 길이가 이전에 계산한 최대 세로 길이보다 크면 업데이트
        if min_side > min_height:
            min_height = min_side
            
    answer = min_width * min_height

    return answer
