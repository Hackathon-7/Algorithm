# 소수 판별 함수
def is_prime(num):
    # 소수: 약수가 1과 자신 뿐인 2 이상의 수
    if num < 2:
        return False
    # num의 약수는 num의 제곱근이상의 수에서 존재하지 않음 
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# 만들 수 있는 수의 경우의 수 찾는 함수
def find_combinations(numbers, used, num, unique_numbers):
    # unique_numbers에 안 들어있거나 0이 아닌 수는 추가
    if num != 0 and num not in unique_numbers and is_prime(num):
        unique_numbers.add(num)
    # numbers 리스트의 모든 숫자를 실행
    for i in range(len(numbers)):
        # 숫자 사용하지 않은 경우만 실행
        if not used[i]:
            # 숫자 사용함
            used[i] = True
            # num에 숫자 더함. 가능한 모든 조합 생성
            find_combinations(numbers, used, num * 10 + int(numbers[i]), unique_numbers)
            # 숫자 사용하지 않음으로 표시 >> 다른 숫자 조합에 사용
            used[i] = False

def solution(numbers):
    answer = set()
    used = [False] * len(numbers)

    find_combinations(numbers, used, 0, answer)

    return len(answer)
