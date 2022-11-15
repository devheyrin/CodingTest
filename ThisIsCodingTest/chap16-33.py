n = int(input())

t = [0]*n
p = [0]*n

for i in range(n):
  t[i], p[i] = map(int, input().split())

dp = [0]*(2*n)

for i in range(n):
  if dp[i] > dp[i+1]:
    dp[i+1] = dp[i]
  if dp[i + t[i]] < dp[i] + p[i]:
    dp[i + t[i]] = dp[i] + p[i]
  print(dp)

print(dp[n])