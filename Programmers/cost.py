# 부족한 금액 계산하기 

def solution(price, money, count):
    cost = 0
    for i in range(1, count+1):
        cost += i*price
    if cost < money:
        return 0
    return cost - money