from itertools import permutations

def is_prime(n):
    # (제곱근 +1)까지만 계산해서 소수인지 판별하는 함수
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def solution(numbers):
    # 소수 숫자
    answer = 0
    # 중복을 거를 set
    nums = set()
    
    # 주어진 숫자들로 만들 수 있는 모든 조합 생성
    for i in range(1, len(numbers) + 1):
        # 순열
        perms = list(permutations(numbers, i))
        for perm in perms:
            
            # 문자열로 이루어진 순열의 숫자들 결합
            # 011은 자동으로 11이 됨.
            num = int(''.join(perm))
            # 중복 거름
            nums.add(num)
    
    # 각 조합이 소수인지 판별
    for num in nums:
        if is_prime(num):
            answer += 1
    
    return answer
