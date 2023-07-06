def solution(citations):
  # 인용 횟수를 내림차순으로 정렬
  citations.sort(reverse=True)
  h_index = 0
  for i in range(len(citations)):
    # 현재 논문의 인용 횟수가 인덱스보다 크거나 같으면 H-Index 갱신
    if citations[i] >= i + 1:
      h_index = i + 1
    else:
      break
  return h_index
