def solution(citations):
    # 인용횟수를 오름차순으로 정렬
    citations.sort()

    # 발표한 논문의 갯수
    n = len(citations)

    for i in range(n):

        # (n-i) = h
        # 작은 순서대로 나오고, 조건을 만족할 때까지 총 논문의 갯수에서 1씩 차감.
        if citations[i] >= n - i:
            return n - i

        # 없으면 0 return
    return 0


