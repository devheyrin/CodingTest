n = int(input())

triangle = [] 
for _ in range(n):
  tmp = list(map(int, input().split()))
  # 빈 공간은 0으로 채운 뒤 triangle에 추가 
  for _ in range(n-len(tmp)):
    tmp.append(0)
  print(tmp)
  triangle.append(tmp)
# print(triangle)

for i in range(n):
  for j in range(n):
    if i == 0:
      # 첫째 행이면 위 칸은 없으므로 0처리 
      up = 0
      left_up = 0
    else:
      # 그 다음 행부터는 위 칸, 왼쪽 위 칸 숫자 각각 구하기 
      up = triangle[i-1][j]
      left_up = triangle[i-1][j-1]
    # 둘 중 최댓값을 구해 현재 칸에 누적   
    triangle[i][j] += max(up, left_up)
    print(*triangle, end='\n')

print(max(triangle[n-1]))


"""
5
7
3 8
8 1 0
2 7 4 4
4 5 2 6 5
"""