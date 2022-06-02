
def solution(new_id:str):
    # 1단계 - 대문자 > 소문자 
    new_id = new_id.lower()

    # 2단계 - 특수문자 제거 
    answer = ''
    for chr in new_id:
        if chr.isalnum() or chr in '-_.':
            answer += chr

    # 3단계 - .가 2번 이상 연속된 부분을 하나의 마침표로 치환
    while '..' in answer:
        answer = answer.replace('..', '.') 
    
    print(answer)

    # 4단계 - .가 처음이나 끝에 위치한다면 제거 
    if answer[0] == '.':
        answer = answer[1:]
    if len(answer) > 1 and answer[-1] == '.':
        answer = answer[:-1]
    if answer == '.':
        answer = ''

    # 5단계 - 빈 문자열이면 a를 대입 
    if not answer:
        answer = 'a'
    # 6단계 - 길이가 16자 이상이면 첫 15개 문자를 제외하고 나머지 모두 제거
    if len(answer) >= 16:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]
    # 7단계 - 길이가 2자 이하라면 new_id 의 마지막 문자를 new_id의 길이가 3일 때까지 반복해서 끝에 붙이기
    while len(answer) <= 2:
        answer += answer[-1]

    return answer


print(solution("abcdefghijklmn.p"))

