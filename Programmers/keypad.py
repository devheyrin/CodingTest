def solution(numbers, hand):

    keypad = {1: (0, 0), 2: (0, 1), 3: (0, 2), 
              4: (1, 0), 5: (1, 1), 6: (1, 2),
              7: (2, 0), 8: (2, 1), 9: (2, 2),
              0: (3, 1)}
    left = (3, 0)
    right = (3, 2)

    answer = ''
    for number in numbers:
        if number in [1, 4, 7]:
            answer += "L"
            left = keypad[number]
        elif number in [3, 6, 9]:
            answer += "R"
            right = keypad[number]
        else:
            x, y = keypad[number]
            left_dist = abs(left[0]-x) + abs(left[1]-y)
            right_dist = abs(right[0]-x) + abs(right[1]-y)
            if left_dist == right_dist:
                if hand == "left":
                    answer += "L"
                    left = keypad[number]
                else:
                    answer += "R"
                    right = keypad[number]
            if left_dist > right_dist:
                answer += "R"
                right = keypad[number]
            elif left_dist < right_dist:
                answer += "L"
                left = keypad[number]
        
    return answer

print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "right"))