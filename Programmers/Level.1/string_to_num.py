def solution(s):
    words = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    anwer = s
    for number, word in enumerate(words):
        anwer = anwer.replace(word, str(number))
    return int(anwer)

print(solution('123'))
