import heapq

INF = 1e9
t = int(input())
for _ in range(t):
  n = int(input())
  graph = []
  for _ in range(n):
    graph.append(list(map(int, input().split())))

  distance = [[INF] * n for _ in range(n)]

  q = []
  heapq.heappush(q, (graph[0][0], 0, 0))
  distance[0][0] = graph[0][0]

  while q:
    dist, x, y = heapq.heappop(q)
    if dist > distance[x][y]:
      continue
    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
      nx = x + dx
      ny = y + dy
      if nx < 0 or nx >= n or ny < 0 or ny >= n:
        continue
      cost = dist + graph[nx][ny]
      if cost < distance[nx][ny]:
        distance[nx][ny] = cost
        heapq.heappush(q, (cost, nx, ny))
  print(distance[n-1][n-1])






