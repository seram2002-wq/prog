def solution(arr):
    n=0
    while 2**n<len(arr):
        n+=1
    while len(arr)<2**n:
        arr.append(0)
    return arr
