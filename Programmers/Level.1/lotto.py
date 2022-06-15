def solution(lottos, win_nums):
    min_win_num = 0
    zero_num = 0

    for num in lottos:
        if num == 0:
            zero_num += 1
        elif num in win_nums:
            min_win_num += 1

    max_win_num = min_win_num + zero_num

    rates = [6, 6, 5, 4, 3, 2, 1]

    answer = [rates[max_win_num], rates[min_win_num]]
    return answer

