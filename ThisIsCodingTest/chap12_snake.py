n = int(input())
k = int(input())

graph = [[0]*(n+1) for _ in range(n+1)]
directions = []
# 사과의 위치
for _ in range(k):
  x, y = map(int, input().split())
  graph[x][y] = 1

print(graph)

# 방향 변환 횟수
l = int(input())
for _ in range(l):
  x, c = input().split()
  directions.append((int(x), c))

i = 0
j = 0
sec = 0
direction = 'D'
while True:
  if i < 0 or i >= n or j < 0 or j >= n:
    break
  if 
