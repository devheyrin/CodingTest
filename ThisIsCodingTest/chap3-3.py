n, m = map(int, input().split())
arr = []
for i in range(n):
  # 행마다 최솟값 구해서 arr에 추가 
  row = list(map(int, input().split()))
  arr.append(min(row))

print(max(arr))





