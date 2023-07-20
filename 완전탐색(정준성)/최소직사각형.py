def solution(sizes):
    # 최대 가로, 최대 세로 길이
    max_width = 0
    max_height = 0
    
    for size in sizes:
        # 사이즈 대입
        width, height = size
        
        # 현재 명함의 가로와 세로 중에서 더 큰 값을 찾음
        if width < height:
            width, height = height, width
        
        # 현재 명함의 가로 길이와 세로 길이가 최대값보다 크다면 갱신
        if width > max_width:
            max_width = width
        if height > max_height:
            max_height = height
    
    return max_width * max_height
