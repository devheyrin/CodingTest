def solution(priorities, location):
    printed = []
    
    priorities = [(i, priorities[i]) for i in range(len(priorities))]
    max_prty = max(priorities, key=lambda x : x[1])[1]

    while priorities:
        max_prty = max(priorities, key=lambda x : x[1])[1]

        if priorities[0][1] != max_prty:
            priorities.append(priorities.pop(0))
        else:
            printed.append(priorities[0][0])
            priorities.pop(0)
            
            
    return printed.index(location) + 1