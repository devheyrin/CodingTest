def solution(answers):
    student_1 = [1, 2, 3, 4, 5]
    student_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    student_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    ans_id = st1_id = st2_id = st3_id = 0 

    scores = [[1, 0], [2, 0], [3, 0]]

    while ans_id != len(answers):
        if student_1[st1_id] == answers[ans_id]:
            scores[0][1] += 1
        if student_2[st2_id] == answers[ans_id]:
            scores[1][1] += 1
        if student_3[st3_id] == answers[ans_id]:
            scores[2][1] += 1
        ans_id += 1
        st1_id = (st1_id+1) % 5
        st2_id = (st2_id+1) % 8
        st3_id = (st3_id+1) % 10
    

    max_score = max(scores, key=lambda x: x[1])[1]

    answer = []
    for id, score in scores:
        if score == max_score:
            answer.append(id) 
               
    return answer

print(solution([1, 3, 2, 4, 2]))
print(solution([1, 2, 3, 4, 5]))