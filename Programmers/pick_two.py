from itertools import combinations


def solution(numbers):
    answer = set(sum(i) for i in combinations(numbers, 2))
    answer = list(answer)
    answer.sort()
    return list(answer)

print(solution([2,1,3,4,1]))
print(solution([5,0,2,7]))
