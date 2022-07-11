n = int(input())
arr_store = list(map(int, input().split()))
arr_store.sort()
m = int(input())
arr_req = list(map(int, input().split()))

def bin_search(arr, target, st, ed):
  while st <= ed:
    mid = (st + ed) // 2
    if arr[mid] == target:
      return mid
    elif arr[mid] > target:
      ed = mid - 1
    else:
      st = mid + 1
  return False
  
for i in arr_req:
  result = bin_search(arr_store, i, 0, n-1)
  if result:
    print('yes', end=' ')
  else:
    print('no', end=' ')