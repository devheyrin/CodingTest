n, m = map(int, input().split())
INF = 1e9
graph = [[INF for _ in range(n+1)] for _ in range(n+1)]


for i in range(n+1):
  graph[i][i] = 0

for _ in range(m):
  a, b = map(int, input().split())
  # a -> b 비용을 1로 설정 
  graph[a][b] = 1


for k in range(1, n+1):
  for i in range(1, n+1):
    for j in range(1, n+1):
        graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])


result = 0
for i in range(1, n+1):
  count = 0
  for j in range(1, n+1):
    if graph[i][j] != INF or graph[j][i] != INF:
      count += 1
  if count == n:
    result += 1

print(result)