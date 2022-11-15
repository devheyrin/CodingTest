import heapq

INF = int(1e9)

n, m = map(int, input().split())

# 1번 헛간에서 출발 
start = 1

# 노드 간의 연결 표현 
graph = [[] for _ in range(n+1)]

# 최단 거리 테이블을 초기화 
# 초기 거리는 무한대로 설정 
distance = [INF] * (n+1)

for _ in range(m):
  a, b = map(int, input().split())
  # 연결된 노드 간의 거리는 모두 1로 초기화 
  graph[a].append((b, 1))
  graph[b].append((a, 1))

def dijkstra(start):
  q = []
  heapq.heappush(q, (0, start))
  distance[start] = 0

  while q:
    # 최단거리가 가장 짧은 노드 꺼내기 
    dist, now = heapq.heappop(q)

    # 꺼낸 거리가 최단거리테이블에 기록된 거리보다 길면
    # 탐색 대상에서 제외! -> 방문 테이블 따로 사용하지 x
    if distance[now] < dist:
      continue
      
    # 현재 노드와 연결된 인접노드 확인 
    for next, d in graph[now]:
      cost = dist + d

      # 최단거리 테이블에 기록된 거리보다 
      # 현재 노드 방문후 거리가 더 짧으면 갱신 
      if cost < distance[next]:
        distance[next] = cost
        heapq.heappush(q, (cost, next))

dijkstra(start)


max_node = 0
max_dist = 0
result = []

# 최단거리 테이블 검사 - 가장 먼 헛간 구하기 
for i in range(1, n+1):
  if max_dist < distance[i]:
    max_node = i
    max_dist = distance[i]
    result = [max_node]
  elif max_dist == distance[i]:
    result.append(i)

# 헛간 번호, 헛간까지의 거리, 헛간의 개수 
print(max_node, max_dist, len(result))