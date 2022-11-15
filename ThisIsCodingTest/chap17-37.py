n = int(input())
m = int(input())
INF = 1e9
bus = [[INF for _ in range(n+1)] for _ in range(n+1)]

for _ in range(m):
  st, ed, cost = map(int, input().split())
  bus[st][ed] = min(cost, bus[st][ed])


for k in range(1, n+1):
  for i in range(1, n+1):
    for j in range(1, n+1):
      if i == j:
        bus[i][j] = 0
      else:
        # i -> j 직행 비용과 k 경유해서 가는 비용을 비교
        bus[i][j] = min(bus[i][j], bus[i][k] + bus[k][j])


for row in bus[1:]:
  for col in row[1:]:
    if col == INF:
      print(0, end=" ")
    else:
      print(col, end=" ")
  print()