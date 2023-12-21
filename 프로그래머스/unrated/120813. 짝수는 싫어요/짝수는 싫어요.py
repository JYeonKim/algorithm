def solution(n):
    if n%2 == 0:
        answer = [idx*2+1 for idx, num in enumerate(range(n//2))]
    else:
        answer = [idx*2+1 for idx, num in enumerate(range(n//2+1))]
    return answer