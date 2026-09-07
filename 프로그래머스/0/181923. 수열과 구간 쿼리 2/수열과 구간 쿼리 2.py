def solution(arr, queries):
    answer = []
    for s,e,k in queries:
        target_values = [arr[i] for i in range(s, e + 1) if arr[i] > k]
        if target_values:
            answer.append(min(target_values))
        else:
            answer.append(-1)
            
    return answer