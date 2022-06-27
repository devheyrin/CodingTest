n, m, k = map(int, input().split())
arr = list(map(int, input().split()))

# n, m, k = 5, 8, 3
# arr = [2, 4, 5, 4, 6]

arr.sort(reverse=True)
max_num = arr[0]
scd_num = arr[1]

# 규칙 찾기 k+1 번에 한 번 두번째로 큰 수를 넣어주어야 한다. 
scd_cnt = m // (k+1)
max_cnt = m - scd_cnt

answer = max_num * max_cnt + scd_num * scd_cnt
print(answer)

# # input
# n, m, k = 5, 8, 3
# arr = [2, 4, 5, 4, 6]

# # input
# n, m, k = 