def solution(myString):
    answer = []
    myString1=myString.split("x")
    for i in myString1:
        if i!="":
            answer.append(i)
            
    answer=sorted(answer)
    return answer
