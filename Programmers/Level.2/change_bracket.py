def solution(p):
    answer = ''
    if not p:
        return ''
    if isWrite(p):
        return p
    
    u, v = seperate(p)

    if isWrite(u):
        return u + solution(v)
    else:
        answer += '('
        answer += solution(v)
        answer += ')'
        if u:
            u = u[1:-1]
            answer += ''.join(reverse(u))
    
    return answer

def isWrite(w):
    arr = [w[0]]
    w = list(w)
    i = 1
    while True:
        if i >= len(w):
            break
        if arr and w[i] == ')' and arr[-1] == '(': 
            arr.pop()
        else:
            arr.append(w[i])
        i += 1
    if not arr:
        return True
    return False
      

def reverse(w):
    r = {"(":")", ")":"("}
    return [r[s] for s in w]

def seperate(w):
    w = list(w)
    u = ''
    v = ''
    left_cnt = 0
    right_cnt = 0
    i = 0
    while True:
        if i >= len(w): break
        if w[i] == '(': left_cnt += 1
        if w[i] == ')': right_cnt += 1
        u += w[i]
        if left_cnt == right_cnt: break
        i += 1
 
    v = ''.join(w[i+1:])
    return u, v