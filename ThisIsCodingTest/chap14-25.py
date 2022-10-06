# 실패 
def solution(n, stages):
    answer = []
    length = len(stages)
    failure = [0] * (n + 1)   #스테이지에 도달한 사람수 담을 배열
    # 해당 스테이지에 머물러 있는 사람 수 계산
    for i in range(1, length + 1):
        if stages[i - 1] == n + 1:
            failure[stages[i - 1] - 1] = 0
        else :
            failure[stages[i - 1]] += 1
    # 각 단계별 실패율 계산
    for i in range(1, n + 1):
        if length == 0 :
            fail = 0
        else :
            fail = failure[i] / length
        answer.append((i, fail))
        length -= failure[i] 
    answer = sorted(answer, key=lambda t: t[1], reverse=True)
    answer = [i[0] for i in answer]
    return answer