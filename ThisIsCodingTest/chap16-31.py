t = int(input())
for _ in range(t):
  n, m = map(int, input().split())
  arr = list(map(int, input().split()))
  gold = [[0]*m for _ in range(n)]
  index = 0
  for i in range(n):
    for j in range(m):
      gold[i][j] = arr[index]
      index += 1
  
	# 현재 위치 와 이전위치 (3가지)의 합 중에서 가장 큰 것을 선택해 현재 금 채굴량을 업데이트한다. 
  for j in range(1, m):
    for i in range(n):
      # 현재 
      now = gold[i][j]
      # 왼쪽 위 
      left_up = gold[i-1][j-1]
      # 왼쪽
      left = gold[i][j-1]
      # 왼쪽 아래
      left_down = gold[i+1][j-1]
      if i == 0:
				# 첫 번째 행의 경우 위쪽 행이 없으므로 왼쪽 위를 제외한 두 방향을 비교 
        gold[i][j] = max(now + left, now + left_down)
      elif i == n-1:
        # 마지막 행의 경우 아래쪽 행이 없으므로 왼쪽 아래를 제외한 두 방향을 비교 
        gold[i][j] = max(now + left_up, now + left)
      else:
        # 그 외의 경우 왼쪽 위, 왼쪽, 왼쪽 아래 모두 비교 
        gold[i][j] = max(now + left_up, now + left, now + left_down)
  
  result = 0
  for g in gold:
    result = max(result, max(g))

  print(result)

"""
2
3 4
1 3 3 2 2 1 4 1 0 6 4 7
4 4
1 3 1 5 2 2 4 1 5 0 2 3 0 6 1 2 
"""