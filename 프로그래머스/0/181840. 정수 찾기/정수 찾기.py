def solution(num_list, n):
    answer = 0
    for num in num_list:
        if n==num:
            answer+=1
            break
    return answer