def solution(sizes):
    w_arr = []
    h_arr = []
    for size in sizes:
        w_arr.append(min(size))
        h_arr.append(max(size))
    print(w_arr)
    print(h_arr)
    answer = max(w_arr) * max(h_arr)
    return answer

print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))
print(solution([[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]))
print(solution([[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]))