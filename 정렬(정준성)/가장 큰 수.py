def solution(numbers):
    # numbers를 문자열로 변환
    str_num = []
    for i in numbers:
        str_num.append(str(i))

    # 두 수를 이어붙였을 때 큰 순서대로 하기 위해 *3 함.
    # 문자열에서는 자릿수에서 더 큰 숫자가 나오는 순서대로 정렬이 되기 때문에,
    # '3'과 '30', '34'의 문자열에 *3를 해서 나오는 '333'과 '303030' '343434'를 비교해보면
    # '343434', '333', '303030' 순으로 정렬이 된다.
    str_num.sort(key=lambda x: x * 3, reverse=True)

    # 만약에 0000이 나왔을 경우, 0으로 출력되게 바꿈.
    if str_num[0] == '0':
        return '0'

    # 문자열 합쳐서 return
    large = ''.join(str_num)

    return large



