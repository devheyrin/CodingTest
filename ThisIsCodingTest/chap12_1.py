# 럭키 스트레이트

# 입력받기 
n = list(map(int, input()))  # '123402'
# 가운데 인덱스 구하기 
mid = len(n) // 2  # 6 / 2 = 3
# 좌우 합 구하기 
left_sum = sum(n[:mid])
right_sum = sum(n[mid:])
# 비교 
if left_sum == right_sum:
  print('LUCKY')
else:
  print('READY')

