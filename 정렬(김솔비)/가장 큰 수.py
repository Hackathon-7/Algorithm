def solution(numbers):
    #int형의 list를 map 사용해서 string으로 치환후, list로 변환
    #sort()를 이용하여 key조건에 맞게 정렬
    numbers = list(map(str, numbers))
    
    #lambda x = x*3은 각각의 문자열을 3번 반복한다는 뜻
    #인수값이 1000이하이기 때문에 3자리수로 맞춤
    #문자열 비교는 아스키 값으로 치환돼서 정렬
    #sort()의 기본 정렬 기준은 오름차순 -> reverse=true를 통해 내림차     순 정렬
    numbers.sort(key=lambda x: x * 3, reverse=True)
    
    #그 후 문자열 합치기
    return str(int(''.join(numbers)))

