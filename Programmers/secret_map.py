# 비밀지도 
def getBinary(num, n):
    binary = ['0']*n
    i = 0
    while True:
        binary[i] = str(num % 2)
        i += 1
        if num // 2:
            num //= 2
            continue
        return binary[::-1]


def solution(n, arr1, arr2):
    secret_map = [''] * n
    for i in range(n):
        row1 = getBinary(arr1[i], n)
        row2 = getBinary(arr2[i], n)
        for j in range(n):
            if int(row1[j]) or int(row2[j]):
                secret_map[i] += '#'
            else:
                secret_map[i] += ' '
    return secret_map

        
print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))
print(solution(6, [46, 33, 33 ,22, 31, 50], [27 ,56, 19, 14, 14, 10]))
