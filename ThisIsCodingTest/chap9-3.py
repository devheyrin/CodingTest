import grp
import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

# 노드의 개수, 간선의 개수, 시작 노드 
n, m, start = map(int, input().split())

# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트 
graph = [[] for _ in range(n+1)]

distance = [INF] * (n+1)

for _ in range(m):
  x, y, z = map(int, input().split())
  graph[x].append((y, z))

def dkstra(start):
  q = []
  # 시작 노드로 가기 위한 최단 경로를 0으로 큐에 삽입 
  heapq.heappush(q, (0, start))
  distance[start] = 0
  while q:
    dist, now = heapq.heappop(q)
    if distance[now] < dist:
      continue
    for i in graph[now]:
      cost = dist + i[1]
      if cost < distance[i[0]]:
        distance[i[0]] = cost
        heapq.heappush(q, (cost, i[0]))

dkstra(start)

# 도달할 수 있는 노드의 개수 
count = 0

# 도달할 수 있는 노드 중에서 가장 멀리 있는 노드와의 최단거리 
max_distance = 0

for d in distance:
  if d != INF:
    count += 1
    max_distance = max(max_distance, d)

print(count - 1, max_distance)
