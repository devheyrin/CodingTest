g = int(input())
p = int(input())

parent = [0] * (g+1)
for i in range(1, g+1):
  parent[i] = i

def find(parent, x):
  if parent[x] != x:
    parent[x] = find(parent, parent[x])
  return parent[x]

def union(parent, a, b):
  a = find(parent, a)
  b = find(parent, b)
  if a < b:
    parent[b] = a
  else:
    parent[a] = b
  
count = 0
for _ in range(p):
  data = find(parent, int(input()))
  if data == 0:
    break
  union(parent, data, data-1)
  count += 1

print(count)