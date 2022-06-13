def solution(dartResult):
    scores = []
    bonuses = {"S" : 1, "D": 2, "T": 3}
    i = 0
    while i < len(dartResult):
        score = int(dartResult[i])
        if dartResult[i+1] == '0':
            score = 10
            i += 1
        bonus = bonuses[dartResult[i+1]]
        option = 1
        scores.append([score, bonus, option])

        i += 2
        if i >= len(dartResult):
            break
        if dartResult[i] == '*':
            if len(scores) == 3:
                scores[2][2] *= 2
                scores[1][2] *= 2
            elif len(scores) == 2:
                scores[1][2] *= 2 
                scores[0][2] *= 2
            else:
                scores[0][2] *= 2
            i += 1
        elif dartResult[i] == '#':
            scores[-1][2] = -1
            i += 1

    answer = 0

    for score, bonus, option in scores:
        answer += score**bonus*option

    return answer

print(solution('1S2D*3T'))
print(solution('1D2S#10S'))
print(solution('1D2S0T'))
print(solution('1S*2T*3S'))
print(solution('1T2D3D#'))
print(solution('0D#2S*3S'))
print(solution('1S2D3T*'))
print(solution('1S2D*3T*'))

