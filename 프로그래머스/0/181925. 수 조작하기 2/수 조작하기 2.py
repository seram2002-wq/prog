def solution(numLog):
    answer = ''
    k={1:'w',-1:'s',10:'d',-10:'a'}
    for j in range(len(numLog)-1):
        diff=numLog[j+1]-numLog[j]
        answer += k[diff]
    return answer

    