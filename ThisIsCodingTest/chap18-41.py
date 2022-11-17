# 최종 부모를 찾는 연산 
def find(parent, x):
  if parent[x] != x:
    parent[x] = find(parent, parent[x])
  return parent[x]

def union(parent, a, b):
  a = find(parent, a)
  b = find(parent, b)

  if a > b:
    parent[a] = b
  else:
    parent[b] = a

n, m = map(int, input().split())
parent = [0] * (n+1)
for i in range(1, n+1):
  parent[i] = i

print(parent)

for i in range(n):
  graph = list(map(int, input().split()))
  for j in range(n):
    if graph[j]:
      union(parent, i, j)

visit = list(map(int, input().split()))

print(parent)

result = False

for i in range(1, m):
  print(i)
  if find(parent, visit[i]) != find(parent, visit[i-1]):
    result = True
    break

if result == True:
  print('NO')
else:
  print('YES')

''' input 
5 4
0 1 0 1 1
1 0 1 1 0
0 1 0 0 0
1 1 0 0 0
1 0 0 0 0
2 3 4 3
'''