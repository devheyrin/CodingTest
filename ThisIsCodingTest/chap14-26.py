# 시간 초과 
import sys
input = sys.stdin.readline
import heapq

n = int(input())
cards = []
for _ in range(n):
  heapq.heappush(cards, int(input()))
  #cards.append(int(input()))

answer = 0

while len(cards) > 1:
  #sum = cards.pop(0) + cards.pop(0)
  sum = heapq.heappop(cards) + heapq.heappop(cards)
  answer += sum
  heapq.heappush(cards, sum)
  #cards.append(sum)
  #cards.sort()

print(answer)

# 
# 
# print(cards)