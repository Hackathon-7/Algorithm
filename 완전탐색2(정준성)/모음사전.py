def solution(word):

  # A, AA, AAA, AAAA, AAAAA의 경우의 수를 더함
    answer = len(word)


   # 각 자리의 경우의 수
    calc = [781, 156, 31, 6, 1]

   # 문자열 순서
    dict = "AEIOU"

    

    for i in range(len(word)):

       # find()는 index를 반환
        answer += dict.find(word[i]) * calc[i]

    return answer


