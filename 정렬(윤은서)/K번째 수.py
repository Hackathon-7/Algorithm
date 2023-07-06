def solution(array, commands):
  answer=[]
  # commands에 존재하는 command가 있는 만큼 반복
  for command in commands:
    # 각 요소를 [i, j, k]에 대입
    i, j, k = command
    # array의 i-1번째부터 j까지 배열 자르기
    new_array = array[i-1:j]
    # 자른 배열 정렬
    sorted_array = sorted(new_array)
    # k번째에 위치한 수 answer에 넣기
    num = sorted_array[k-1]
    answer.append(num)
  return answer
