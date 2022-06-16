def solution(new_id):
    answer = ''
    # 1단계 
    answer = new_id.lower()
    # print(1, answer)
    # 2단계
    answer = list(answer)
    new_answer = ''
    for i in answer:
        if i.isalnum() or i in ['-', '_', '.']:
            new_answer += i
    # print(2, new_answer)
    # 3단계
    cnt = 0
    answer = ''
    for i in new_answer:
        if i == '.':
            cnt += 1
        else:
            cnt = 0
        if cnt > 1:
            continue
        answer += i  
    # print(3, answer)

    # 4단계 
    if answer[0] == '.':
        answer = answer[1:]
    # print(4, answer)
    if answer and answer[-1] == '.':
        answer = answer[:-1]
    # print(4, answer)

    # 5단계 
    if not answer:
        answer += 'a'
    # print(5, answer)

    # 6단계
    if len(answer) >= 16:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]

    # 7단계
    if len(answer) <= 2:
        while len(answer) != 3:
            answer += answer[-1]
    # print(answer)


    return answer