def solution(n):
    answer = 0
    if n%2==1:
        for i in range(1,n+1,2):
            answer+=i
    else:
        for k in range(2,n+1,2):
            answer+=k**2
    return answer