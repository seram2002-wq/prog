def solution(rank, attendance):
    answer = 0
    possible=[]
    for i in range(len(rank)):
        if attendance[i]:
            possible.append((rank[i],i))
    possible.sort()
    answer=possible[0][1]*10000+possible[1][1]*100+possible[2][1]
    return answer