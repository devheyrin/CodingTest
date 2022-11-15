a = input()
b = input()
a_len = len(a)
b_len = len(a)

dp = [[0] * (b_len+1) for _ in range(a_len + 1)]
for i in range(1, a_len+1):
  dp[i][0] = i
for j in range(1, b_len+1):
  dp[0][j] = j

for i in range(1, a_len+1):
  for j in range(1, b_len+1):
    if a[i-1] == b[j-1]:
      dp[i][j] = dp[i-1][j-1]
    else:
      dp[i][j] = 1 + min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1])

for i in dp:
  for j in i:
    print(j, end=" ")
  print("")

print(dp[a_len][b_len])

