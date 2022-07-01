from itertools import combinations

def solution(relation):
    row = len(relation)
    col = len(relation[0])

    # 가능한 키 조합 모두 구하기 
    all_key = []
    for i in range(col):
        temp = list(combinations([str(i) for i in range(col)], i+1))
        all_key += temp
    
    all_key = [''.join(i) for i in all_key]
        

    # 유일성 만족 키 구하기 
    # 키 조합별 튜플(행)을 모두 구한 뒤, set을 취해 중복을 제거 
    # 중복 제거 후 길이가 relation과 같으면 유일성을 만족 
    uniq_key = []
    for key in all_key:
        temp = ['' for _ in range(row)]
        for i in key:
            i = int(i)
            for j in range(row):
                temp[j] += relation[j][i]

        # 중복 제거 후 길이 비교해 유일성 만족하는 키만 선별 
        if len(set(temp)) == len(relation):
            uniq_key.append(key)


    # 최소성 만족 키 구하기         
    i = 0
    while True:
        if i >= len(uniq_key):
            break
        # i번째 키를 제외하고 검사 
        for j in uniq_key[i+1:]:
            # 02, 012 와 같은 경우를 걸러내기 위해 set 이용 
            # A의 모든 요소가 B에 포함되면 set() - False 반환 
            # 이에 해당하는 키를 uniq_key 리스트에서 삭제 
            if not set(list(uniq_key[i])) - set(list(j)):
                uniq_key.remove(j)
        i += 1

    return len(uniq_key)