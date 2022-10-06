# 치킨 거리가 작은 순으로 m개를 선택 
# 치킨 거리 : 각각의 집을 기준으로 가장 가까운 치킨집까지의 거리 
# 도시의 치킨거리 : 모든 집의 치킨 거리의 합 

from itertools import combinations

n, m = map(int, input().split())
graph = []

# 입력받기
for _ in range(n):
  graph.append(list(map(int, input().split())))

# 치킨집 좌표 리스트 구하기 
chicken_shop_arr = []
for i in range(n):
  for j in range(n):
    if graph[i][j] == 2:
      chicken_shop_arr.append((i, j))

# 폐업시키지 않을 치킨집 조합 구하기 
chicken_shop_combi = list(combinations(chicken_shop_arr, m))

# 최단치킨거리를 구하는 함수 
def get_min_chicken_dist(x, y, combi):
  min_chicken_dist = 1e9
  for i, j in combi:
    dist = abs(x - i) + abs(y - j)
    min_chicken_dist = min(min_chicken_dist, dist)
  return min_chicken_dist

# 가능한 치킨집 조합 별 도시 치킨거리합 구하기 
result = 1e9
for combi in chicken_shop_combi:
  chicken_dist = []
  for i in range(n):
    for j in range(n):
      if graph[i][j] == 1: # 집 
        mcd = get_min_chicken_dist(i, j, combi)
        chicken_dist.append(mcd)
  result = min(result, sum(chicken_dist))

print(result)


  
