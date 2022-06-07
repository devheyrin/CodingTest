def solution(a, b):
    answer = 0
    for i in range(len(a)):
        answer += a[i]*b[i]
    return answer

print(solution([-1, 0, 1], [1, 0, -1]))