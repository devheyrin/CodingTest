def solution(participant, completion):
    parti_dict = dict(zip(participant, [0]*len(participant)))
    for name in participant:
        parti_dict[name] += 1
    for name in completion:
        parti_dict[name] -= 1
    for key, val in parti_dict.items():
        if val:
            return key
        
print(solution(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"]))