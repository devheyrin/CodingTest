n = int(input())

arr = [0]*n
arr[0] = 1

id2 = id3 = id5 = 0
next2, next3, next5 = 2, 3, 5

for i in range(1, n):
  arr[i] = min(next2, next3, next5)
  if arr[i] == next2:
    id2 += 1
    next2 = arr[id2] * 2
  if arr[i] == next3:
    id3 += 1
    next3 = arr[id3] * 3
  if arr[i] == next5:
    id5 += 1
    next5 = arr[id5] * 5

print(arr[n-1])




