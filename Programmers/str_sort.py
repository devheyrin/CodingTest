def solution(s):

    temp = [ord(i) for i in s]
    temp.sort(reverse=True)
    answer = [chr(i) for i in temp]
    
    return ''.join(answer)