def solution(a, d, included):
    answer = 0
    for k in range(len(included)):
        term = a + d * k
        if included[k]:
            answer+=term
    return answer
     