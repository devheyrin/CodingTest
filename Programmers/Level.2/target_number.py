from collections import deque

def solution(numbers, target):
    answer = 0
    queue = deque()
    queue.append('+')
    queue.append('-')
    
    while queue:
        op = queue.popleft()
        
        if len(op) == len(numbers):
            
            total = 0
            for i in range(len(numbers)):
                if op[i] == '+':
                    total += numbers[i]
                if op[i] == '-':
                    total -= numbers[i]
            if total == target:
                answer += 1

            continue
            
        queue.append(op + '+')
        queue.append(op + '-')
    
    return answer