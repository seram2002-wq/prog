def union(a,b):
    answer = True
    if a==True or b==True:
        answer=True
    else:
        answer=False
    return answer    
def intersection(a,b):
    answer = True
    if a==True and b==True:
        answer=True
    else:
        answer=False        
    return answer

def solution(x1, x2, x3, x4):
    answer = True
    a=union(x1,x2)
    b=union(x3,x4)
    answer=intersection(a,b)
    return answer