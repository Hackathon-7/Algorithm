def solution(brown, yellow):
    total = brown + yellow  # 전체 카펫의 격자 개수

    # 전체 격자 개수의 약수 찾기 (가로길이는 세로길이 이상)
    for height in range(1, int(total**0.5) + 1):
        if total % height == 0:
            width = total // height

            # 노란색 격자 개수를 만족하는지 검사
            if (width-2) * (height-2) == yellow:
                return [width, height]