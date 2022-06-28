n, m = map(int, input().split())

x, y, d = map(int, input().split())

# 맵 - 0은 육지, 1은 바다 
graph = []
for _ in range(n):
  graph.append(list(map(int, input().split())))

# 방문 가능 칸
steps = {0: (-1, 0), 1: (0, 1), 2: (1, 0), 3: (0, -1)}

graph[x][y] = 1 # 시작점 방문 처리 

visit_cnt = 1

def turn_left(d):
  return (d + 1) % 4

while True:
  for _ in range(4):
    left = turn_left(d)
    dx, dy = steps[left]
    nx, ny = x + dx, y + dy

    # 바다로 되어 있는 칸이면 pass
    if nx < 0 or nx >= n or ny < 0 or ny >= m:
      continue

    # 이미 가본 칸이거나 바다로 되어 있는 칸이면 pass
    if graph[nx][ny] == 1:
      continue

    # 한 칸 전진 
    x, y = nx, ny
    # 왼쪽으로 회전 
    d = left
    # 방문 처리 
    graph[x][y] = 1
    visit_cnt += 1

  # 네 방향 모두 이미 가본 칸이거나 바다로 되어 있는 경우 
  dx, dy = steps[d]
  nx, ny = x - dx, y - dy

  # 바다여서 갈 수 없으면 break
  if nx < 0 or nx >= n or ny < 0 or ny >= m:
    break
  if graph[nx][ny] == 1:
    break

  # 한 칸 뒤로 
  x, y = nx, ny
  # 방문 처리 
  graph[x][y] = 1
  visit_cnt += 1

print(visit_cnt)


  



