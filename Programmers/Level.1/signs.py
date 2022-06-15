def solution(absolutes, signs):
    for index, sign in enumerate(signs):
        if not sign:
            absolutes[index] = -absolutes[index]
    return sum(absolutes)

ans = solution([4, 7, 12], [True, False, True])
print(ans)