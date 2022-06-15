def solution(s):
    words = s.split()
    arr = list(s)
    cnt = 0
    i = 0
    while True:
        if arr[i] == ' ':
            i += 1
            continue
            
        word = words[cnt]
        
        for j in range(len(word)):
            word = list(word)
            if j % 2:  # 홀수 
                word[j] = word[j].lower()
            else:
                word[j] = word[j].upper()
       
        arr[i:i+len(word)] = word
        i += len(word)
        if i >= len(arr):
            break
        cnt += 1
        if cnt >= len(words):
            break
                
    
    return ''.join(arr)