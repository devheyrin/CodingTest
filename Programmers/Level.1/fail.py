def solution(N, stages):
    temp = []
    for i in range(1, N+1):
        stage_reach = len([x for x in stages if x >= i])
        stage_nonclear = stages.count(i)

        fail_rate = 0
        if 0 not in (stage_reach, stage_nonclear):
            fail_rate =  stage_nonclear / stage_reach 
        
        temp.append((i, fail_rate))
    temp.sort(key=lambda x: x[1], reverse=True)        
    answer = [i[0] for i in temp]    
    return answer

print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
print(solution(4, [4,4,4,4,4]))