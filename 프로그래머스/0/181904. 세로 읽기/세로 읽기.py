def solution(my_string, m, c):
    answer = ''
    for n in range(len(my_string)//m):
        answer+=my_string[n*m+c-1]
    return answer