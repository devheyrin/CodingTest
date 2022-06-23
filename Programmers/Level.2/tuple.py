def solution(s):
    answer = []
    s = s[2:-2].split('},{')

    s.sort(key=lambda x: len(x))
    prev = set([])
    for i in s:
        temp = set(i.split(','))
        answer.append(int(list(temp - prev)[0]))
        prev = temp

    return answer