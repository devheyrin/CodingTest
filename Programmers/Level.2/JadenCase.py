def solution(s):
    answer = s[0].upper()
    for i in range(1, len(s)):
        if s[i-1] == ' ':
            result = s[i].upper()
            answer += result
        else:
            result = s[i].lower()
            answer += result
    return answer