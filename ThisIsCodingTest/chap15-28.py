n = int(input())
arr = list(map(int, input().split()))

def bin_search(arr, st, ed):
  if st > ed:
    return None
  mid = (st + ed) // 2
  # 고정점을 찾은 경우
  if arr[mid] == mid:
    return mid
  elif arr[mid] > mid:
    return bin_search(arr, st, mid-1)
  else:
    return bin_search(arr, mid + 1, ed)

index = bin_search(arr, 0, n-1)

if index == None:
  print(-1)
else:
  print(index)