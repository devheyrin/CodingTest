steps = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]

y, x = list(input())

y = ord(y) - 97
x = int(x) - 1

answer = 0

for dx, dy in steps:
  nx = x + dx
  ny = y + dy
  # 범위 체크 
  if nx < 0 or nx >= 8 or ny < 0 or ny >= 8:
    continue
  answer += 1

print(answer)