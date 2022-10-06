n, x = map(int, input().split())
arr = list(map(int, input().split()))

def get_first(arr, target, st, ed):
  if st > ed:
    return None
  mid = (st + ed) // 2
  if (mid == 0 or target > arr[mid - 1]) and arr[mid] == target:
    return mid
  elif arr[mid] >= target:
    return get_first(arr, target, st, mid - 1)
  else:
    return get_first(arr, target, mid+1, ed)
  
def get_last(arr, target, st, ed):
  if st > ed:
    return None
  mid = (st + ed) // 2
  if (mid == n-1 or target < arr[mid + 1]) and arr[mid] == target:
    return mid
  elif arr[mid] > target:
    return get_last(arr, target, st, mid - 1)
  else:
    return get_last(arr, target, mid+1, ed)

def count(arr, x):
  n = len(arr)
  first = get_first(arr, x, 0, n-1)

  if first == None:
    return 0
  
  last = get_last(arr, x, 0, n-1)

  return last - first +1

cnt = count(arr, x)

if cnt == 0:
  print(-1)
else:
  print(cnt)