
from collections import deque


n, k = map(int, input().split())
graph = []
for _ in range(n):
  graph.append(list(map(int, input().split())))
# sec초 뒤에 x, y에 존재하는 바이러스의 종류 출력하기 
sec, tx, ty = map(int, input().split())

# 바이러스 정보 기록 (바이러스번호, 시간, 좌표)
virus_info = []
for i in range(n):
  for j in range(n):
    if graph[i][j] != 0:
      virus_info.append((graph[i][j], 0, i, j))

# 바이러스 번호 낮은순으로 정렬 후 큐에 추가 
virus_info.sort() 
queue = deque(virus_info)

while queue:
  virus, s, x, y = queue.popleft()
  if s == sec:
    break
  for dx, dy in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
    nx = x + dx
    ny = y + dy
    if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue
    if graph[nx][ny] == 0:
        graph[nx][ny] = virus
        queue.append((virus, s+1, nx, ny))


print(graph[tx-1][ty-1])



