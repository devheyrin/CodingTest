INF = int(1e9)

n = int(input())
m = int(input())

# 2차원 리스트를 만들고, 모든 값을 무한으로 초기화 
graph = [[INF] * (n+1) for _ in range(n+1)]

for a in range(1, n+1):
  for b in range(1, n+1):
    if a == b:
      graph[a][b] = 0

for _ in range(m):
  # A에서 B로 가는 비용은 C라고 설정 
  a, b, c = map(int, input().split())
  graph[a][b] = c

for k in range(1, n+1):
  for a in range(1, n+1):
    for b in range(1, n+1):
      graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])


for a in range(1, n+1):
  for b in range(1, n+1):
    if graph[a][b] == INF:
      print("INF", end= " ")
    else:
      print(graph[a][b], end=" ")
  print()