def solution(intStrs, k, s, l):
    answer = []
    for num_str in intStrs:
        x=int(num_str[s:s+l])
        if x>k:
            answer.append(x)
    return answer