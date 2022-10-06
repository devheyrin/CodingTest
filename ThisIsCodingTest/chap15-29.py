n, c = map(int, input().split())
arr = []
for _ in range(n):
  arr.append(int(input()))

arr.sort()
print(arr)

start = 1
end = arr[-1] - arr[0]
result = 0

while (start <= end) :
  mid = (start + end) // 2
  
  cnt = 1
  prev = arr[0]
  for i in range(n) :
    if arr[i] - prev >= mid:
      cnt += 1
      prev = arr[i]
  
  if cnt >= c :
    result = max(result, mid)
    start = mid + 1
  else:
    end = mid - 1

print(result)