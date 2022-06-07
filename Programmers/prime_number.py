from itertools import combinations

def isPrimeNum(num):
    for i in range(2, num):
        if num%i == 0:
            return False
    return True

def solution(nums):
    candidates = list(combinations(nums, 3))
    print(candidates)
    answer = 0
    for combi in candidates:
        sum_of_combi = sum(combi)
        if isPrimeNum(sum_of_combi):
            answer += 1
    return answer

print(solution([1,2,7,6,4]))
