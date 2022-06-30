n, m = map(int, input().split())
graph = []
for _ in range(n):
  graph.append(list(map(int, input())))


def dfs(x, y, graph):
  directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
  for dx, dy in directions:
    nx = x + dx
    ny = y + dy
    if nx < 0 or nx >= n or ny < 0 or ny >= m:
      continue
    if graph[nx][ny] == 1:
      continue
    graph[nx][ny] = 1
    dfs(nx, ny, graph)
  return True

answer = 0
for i in range(n):
  for j in range(m):
    if graph[i][j] == 0:
      if dfs(i, j, graph):
        answer += 1

print(answer)