# 입력 받기 
S = input()
# 알파벳 배열, 숫자합 변수 초기화 
alphabet_arr = []
nums_sum = 0

# 알파벳 대문자이면 알파벳 배열에 추가
# 숫자이면 숫자합 변수에 누적합 
for i in S:
  if ord(i) >= 65 and ord(i) <= 90:
    alphabet_arr.append(i)
  else:
    nums_sum += int(i)

# 알파벳 배열 오름차순 정렬 
alphabet_arr.sort()

for i in alphabet_arr:
  print(i, end='')
print(nums_sum)

# AJKDLSI412K4JSJ9D
# K1KA5CB7