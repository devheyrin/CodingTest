# 시간 초과 

from itertools import permutations


def solution(numbers):
    answers = []
    candidates = list(permutations(numbers, len(numbers)))
    for can in candidates:
        can = list(map(str, can))
        answers.append(int(''.join(can)))
    
    return str(max(answers))