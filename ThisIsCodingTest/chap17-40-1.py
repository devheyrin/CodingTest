import heapq

n, m = map(int, input().split())
INF = 1e9 

# 간선 테이블 - 노드 개수+1만큼 준비 
graph = [[] for _ in range(n+1)]

# 최단거리 테이블 
distance = [INF]*(n+1)

# 간선 테이블 채우기 - 각 노드간 거리는 모두 1 
for _ in range(m):
  a, b = map(int, input().split())
  graph[a].append((b, 1))
  graph[b].append((a, 1))

def dijkstra(start):
  q = []
  heapq.heappush(q, (0, start))
  distance[start] = 0


  while q:
    # 힙에 들어있는 노드 중 가장 가까운 노드 반환
    dist, now = heapq.heappop(q)
    
    # 방문 여부 확인 
    if dist > distance[now]:
      continue

    # 현재 노드와 연결된 노드(다음노드)를 검사 
    for next, d in graph[now]:
      cost = dist + d
      if distance[next] > cost:
        distance[next] = cost
        heapq.heappush(q, (cost, next))


start = 1
dijkstra(start)

print(distance)

max_node = 0
max_dist = 0
result = []

for i in range(1, n+1):
  if distance[i] > max_dist:
    max_node = i
    max_dist = distance[i]
    result = [max_node]
  elif distance[i] == max_dist:
    result.append(i)

print(max_node, max_dist, len(result))