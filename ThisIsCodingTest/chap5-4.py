from collections import deque


n, m = map(int, input().split())
graph = []
for _ in range(n):
  graph.append(list(map(int, input())))

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def bfs():
  queue = deque([(0, 0)])
  while queue:
    x, y = queue.popleft()
    for dx, dy in directions:
      nx, ny = x + dx, y + dy
      if nx < 0 or nx >= n or ny < 0 or ny >= m:
        continue
      if graph[nx][ny] != 1:
        continue
      graph[nx][ny] = graph[x][y] + 1
      queue.append((nx, ny))

bfs()
print(graph[n-1][m-1])

