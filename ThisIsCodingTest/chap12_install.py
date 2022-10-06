def possible(answer):
    for x, y, s in answer:
        if s == 0:
            if y == 0 or [x-1, y, 1] in answer or [x, y, 1] in answer or [x, y-1, 0] in answer:
                continue
            return False
        elif s == 1:
            if [x, y-1, 0] in answer or [x+1, y-1, 0] in answer or ([x-1, y,1] in answer and [x+1, y, 1] in answer):
                continue
            return False
    return True
 
def solution(n, build_frame):
    answer = []
    for x, y, a, b in build_frame:
        if b == 1: # 설치
            answer.append([x, y, a])
            if not possible(answer):
                answer.remove([x, y, a])
        if b == 0: # 삭제 
            answer.remove([x, y, a])
            if not possible(answer):
                answer.append([x, y, a])
    answer.sort()
    #print(answer)
    return answer