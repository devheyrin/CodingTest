n, k = map(int, input().split())

answer = 0
while n > 1:
  answer += n % k
  n = n // k
  answer += 1

print(answer)