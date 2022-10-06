from collections import deque
import sys
input = sys.stdin.readline

n, m, k, x = map(int, input().split())
# k - 최단 거리 
# x - 출발 도시 

graph = [[] for _ in range(n+1)]
dist = [0]*(n+1)
visited = [0]*(n+1)

for _ in range(m):
  a, b = map(int, input().split())
  # a 에서 갈 수 있는 도시 추가 
  graph[a].append(b)

def bfs(start):
  visited[start] = 1
  queue = deque([start])
  while queue:
    city = queue.popleft()
    for next in graph[city]:
      # next : city에서 갈 수 있는 도시들
      if visited[next]:
        continue
      visited[next] = 1  # 방문 처리 
      dist[next] = dist[city] + 1  # 현재까지 최단거리 + 1
      queue.append(next)  # 큐에 추가 

bfs(x)

if k not in dist:
  # 최단거리 k가 없으면 -1반환
  print(-1)
else:
  for i in range(n+1):
    if dist[i] == k:
      print(i)