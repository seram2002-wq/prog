def solution(my_string, is_suffix):
    answer = 0
    n=len(my_string)-len(is_suffix)
    if my_string[n:]==is_suffix:
        answer+=1
    return answer