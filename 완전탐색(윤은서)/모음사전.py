def generate_words():
    vowels = "AEIOU"
    words = []
    for v1 in vowels:
        words.append(v1)
        for v2 in vowels:
            words.append(v1 + v2)
            for v3 in vowels:
                words.append(v1 + v2 + v3)
                for v4 in vowels:
                    words.append(v1 + v2 + v3 + v4)
                    for v5 in vowels:
                        words.append(v1 + v2 + v3 + v4 + v5)
    return words

def solution(word):
    words = generate_words()
    # words를순서대로 정렬 
    words.sort()
    # 리스트 words에서 주어진 단어가 등장하는 인덱스를 찾음 
    answer = words.index(word) + 1
    return answer
