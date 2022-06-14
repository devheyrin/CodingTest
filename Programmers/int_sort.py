def solution(n):
    arr = list(map(int, str(n)))
    arr.sort(reverse=True)
    arr = list(map(str, arr))
    
    return int(''.join(arr))