def solution(numbers):
  # numbers를 문자열로 변환
  numbers = list(map(str, numbers))
  
  # 문자열 3번 반복 후 비교 및 정렬
  sorted_numbers = sorted(numbers, key=lambda x: x * 3, reverse=True)
  
  # 가장 큰 수로 이어붙여서 문자열로 반환
  answer = ''.join(sorted_numbers)
  
  # answer가 '0'으로만 이루어진 경우에는 '0'을 반환
  return answer if answer[0] != '0' else '0'
