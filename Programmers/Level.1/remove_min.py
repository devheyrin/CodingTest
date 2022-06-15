def solution(arr):
    answer = []
    min_val = min(arr)
    arr.remove(min_val)

    if not arr:
        return [-1]
    return arr