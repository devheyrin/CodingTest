def solution(progresses, speeds):
    answer = []
    while True:
    
        if not progresses:
            return answer

        cnt = 0
        for i in range(len(progresses)):
            if progresses[i] == 100:
                cnt += 1
            else:
                break
                
        if cnt:
            answer.append(cnt)
            progresses = progresses[cnt:]
            speeds = speeds[cnt:]
        
        for i in range(len(progresses)):
            if progresses[i] + speeds[i] >= 100:
                progresses[i] = 100
            else:
                progresses[i] += speeds[i]