n, m = map(int, input().split())
arr = list(map(int, input().split()))

st = 0
ed = max(arr)

result = 0

while st <= ed:
  mid = (st + ed) // 2
  total = 0
  for i in arr:
    if i > mid:
      total += i - mid
  if total < m:
    ed = mid - 1
  else:
    result = mid
    st = mid + 1

print(result)


