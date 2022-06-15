def solution(n):
    answer = '수'
    for i in range(1, n):
        if answer[-1] == '수':  
            answer += '박'
        else:
            answer += '수'
    return answer