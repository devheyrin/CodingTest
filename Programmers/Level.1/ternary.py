def solution(n):
    ternary = getTernary(n)
    decimal = getDecimal(ternary)
    return decimal

def getTernary(n):
    answer = ''
    while True:
        answer += str(n % 3)
        if n // 3 == 0:
            break
        n //= 3
    return answer[::-1]

def getDecimal(n):
    answer = 0
    for index, num in enumerate(n):
        answer += int(num) * (3**index)
    return answer

print(solution(45))
print(solution(125))