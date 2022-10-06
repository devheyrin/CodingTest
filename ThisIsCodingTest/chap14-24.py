import sys
input = sys.stdin.readline

n = int(input())
house = list(map(int, input().split()))
house.sort()
if n%2: # 홀수인경우
  print(house[n//2])
else:
  print(house[n//2-1])

# min_dist = []

# for i in range(n):
#   dist_sum = 0
#   for j in range(n):
#     dist_sum += abs(house[i] - house[j])
#   min_dist.append((house[i], dist_sum))

# min_dist.sort(key=lambda x:(x[1], x[0]))
# print(min_dist[0][0])