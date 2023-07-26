def solution(brown, yellow):
    total_cells = brown + yellow
    # 3부터 가로 길이(>=세로 길이) 증가
    for width in range(3, total_cells // 3 + 1):
        if total_cells % width == 0:
            height = total_cells // width
            # 노란색 크기==(가로-2)*(세로-2)
            if (width - 2) * (height - 2) == yellow:
                return [height, width]
