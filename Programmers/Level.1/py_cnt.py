def solution(s):
    s = s.lower()
    print(s)
    p_cnt = sum([1 for i in s if i == 'p'])
    y_cnt = sum([1 for i in s if i == 'y'])

    if p_cnt == y_cnt:
        return True
    
    return False