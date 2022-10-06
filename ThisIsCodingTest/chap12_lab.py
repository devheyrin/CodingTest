from copy import copy
from itertools import combinations
from collections import deque

import sys
input = sys.stdin.readline

# 벽 세우기 함수
def build_war(lab, wars):
  # wars - 벽 3개 조합
  for x, y in wars:
    # x, y - 벽 좌표
    lab[x][y] = 1
  return lab

# 바이러스 퍼트리기 
def bfs(virus, lab):
  # 바이러스 있던 좌표로 초기화 
  queue = deque(virus)
  while queue:
    x, y = queue.popleft()
    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
      nx = x + dx
      ny = y + dy
      if nx < 0 or nx >= n or ny < 0 or ny >= m:
        continue
      # 바이러스 퍼트리기 
      if lab[nx][ny] == 0:
        lab[nx][ny] = 2
        queue.append((nx, ny))
  return lab


  

n, m = map(int, input().split())
graph = []
for _ in range(n):
  graph.append(list(map(int, input().split())))


virus = []
temp = []
for i in range(n):
  for j in range(m):
    if graph[i][j] == 2:
      # 바이러스 좌표 구하기 
      virus.append((i, j))
    if graph[i][j] == 0: 
      # 벽을 세울 수 있는 좌표 구하기 
      temp.append((i, j))

# 벽 조합 구하기 
combis = list(combinations(temp, 3))

ans = 0
for wars in combis:
  # 복사본 생성
  lab = [item[:] for item in graph]
  # 벽 세우기 
  new_graph = build_war(lab, wars)
  result = bfs(virus, new_graph)
  # 안전 영역 개수 세기 
  total = 0
  for i in range(n):
    for j in range(m):
      if result[i][j] == 0:
        total += 1
  
  ans = max(ans, total)
  
print(ans)