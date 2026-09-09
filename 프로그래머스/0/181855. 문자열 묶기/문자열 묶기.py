def solution(strArr):
    k=[]
    for i in strArr:
        k.append(len(i))
    max_count=0
    for length in range(1, 31):
        cnt = k.count(length)
        if cnt > max_count:
            max_count = cnt
            
    return max_count