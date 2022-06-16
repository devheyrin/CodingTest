from itertools import combinations 
    

def solution(orders, course):
    answer = []
    menu_dict = {}
    for order in orders:
        for i in course:
            candidates = list(combinations(order, i))
            for can in candidates:
                arr = sorted(list(can))
                can = tuple(arr)
                if can not in menu_dict:
                    menu_dict[can] = 1
                else:
                    menu_dict[can] += 1
    tmp = []      
    
    for key in menu_dict:
        if menu_dict[key] == 1:
            continue
        tmp.append([key, menu_dict[key]])

    for i in course:
        max_val = 0
        arr = [j for j in tmp if len(j[0]) == i]
        arr_sorted = sorted(arr, key=lambda x: x[1], reverse=True)
    
        if arr_sorted:
            max_val = arr_sorted[0][1]
       
            
        for item in arr_sorted:
            if max_val == item[1]:

                answer.append("".join(item[0]))
        
    
    return sorted(answer)