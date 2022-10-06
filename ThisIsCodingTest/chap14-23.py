n = int(input())
arr = []

for _ in range(n):
  name, kor, eng, mat = input().split()
  kor = int(kor)
  eng = int(eng)
  mat = int(mat)
  arr.append((name, kor, eng, mat))

arr = sorted(arr, key=lambda x:(-x[1], x[2], -x[3], x[0]))

for i in range(n):
  print(arr[i][0])