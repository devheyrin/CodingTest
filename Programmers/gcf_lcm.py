def solution(n, m):
    answer = 0
    gcf = 0 # 최대공약수
    lcm = 0 # 최소공배수 
    for i in reversed(range(1, min(n, m)+1)):
        if n % i == 0 and m % i == 0:
            gcf = i
            break
    for i in range(min(n, m), n*m+1):
        if i % n == 0 and i % m == 0:
            lcm = i
            break
    
    return [gcf, lcm]