def solution(s, n):
    answer = ''
    # a 97, z 122, A 65, Z 90
    lower = list(range(97, 123))
    upper = list(range(65, 91))
    
    for i in s:
        if ord(i) == 32:
            answer += ' '
        elif i.islower():
            answer += chr(lower[((ord(i) + n) - 97) % 26])
        elif i.isupper():
            answer += chr(upper[((ord(i) + n) - 65) % 26])
            
    return answer