n, m = map(int, input().split())

x, y, d = map(int, input().split())

# 맵 - 0은 육지, 1은 바다 
graph = []
for _ in range(n):
  graph.append(list(map(int, input().split())))

visited = [[0]*m for _ in range(n)]

# 방문 가능 칸
steps = {0: (-1, 0), 1: (0, 1), 2: (1, 0), 3: (0, -1)}

graph[x][y] = 1 # 시작점 방문 처리 

visit_cnt = 1
turn_time = 0

# 왼쪽으로 회전 
def turn_left():
  global d
  d -= 1
  if d == -1:
    d = 3

while True:
  turn_left() 
  dx, dy = steps[d]
  nx, ny = x + dx, y + dy

  if graph[nx][ny] == 0 and visited[nx][ny] == 0:
    x, y = nx, ny
    # 방문 처리 
    visited[x][y] = 1
    visit_cnt += 1
    turn_time = 0
    continue

  else:
    turn_time += 1
  
  if turn_time == 4:
    # 네 방향 모두 이미 가본 칸이거나 바다로 되어 있는 경우 
    dx, dy = steps[d]
    nx, ny = x - dx, y - dy

    if graph[nx][ny] == 0:
      x, y = nx, ny
    # 한 칸 뒤로 
    else:
      break
    turn_time = 0

print(visit_cnt)