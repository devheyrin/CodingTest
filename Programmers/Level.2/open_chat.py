def solution(record):
    tmp = []
    user_dict = {}
    uid_arr = []
    
    for r in record:
        if r[0] == 'L':
            word, uid = r.split()
            tmp.append(['L', uid])
        if r[0] == 'E':
            word, uid, nickname = r.split()
            if uid not in uid_arr:
                tmp.append(['E', uid])
                user_dict[uid] = nickname
            else:
                user_dict[uid] = nickname
        if r[0] == 'C':
            word, uid, nickname = r.split()
            user_dict[uid] = nickname
            
    answer = []
    for word, uid in tmp:
        if word == 'E':
            answer.append(f'{user_dict[uid]}님이 들어왔습니다.')
        else:
            answer.append(f'{user_dict[uid]}님이 나갔습니다.')

    return answer