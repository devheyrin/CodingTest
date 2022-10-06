import sys
input = sys.stdin.readline

N = int(input())
N_arr = list(map(int, input().split()))
op = list(map(int, input().split()))
maximum = -1e9
minimum = 1e9

def dfs(cnt, total, plus, minus, mul, div):
    global maximum, minimum
    if cnt == N:
        maximum = max(total, maximum)
        minimum = min(total, minimum)
        return 
    if plus:
        dfs(cnt + 1, total + N_arr[cnt], plus - 1, minus, mul, div)
    if minus:
        dfs(cnt + 1, total - N_arr[cnt], plus, minus - 1, mul, div)
    if mul:
        dfs(cnt + 1, total * N_arr[cnt], plus, minus, mul - 1, div)
    if div:
        dfs(cnt + 1, int(total / N_arr[cnt]), plus, minus, mul, div - 1)

dfs(1, N_arr[0], op[0], op[1], op[2], op[3])
print(maximum)
print(minimum)
