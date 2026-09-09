def solution(arr, k):
    answer = []
    seen = set() 
    for num in arr:
        if num not in seen and len(answer)<k:
            seen.add(num)
            answer.append(num)
    while len(answer)<k:
        answer.append(-1)
    return answer