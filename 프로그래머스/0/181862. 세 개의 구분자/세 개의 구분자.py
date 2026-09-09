def solution(myStr):
    answer = []
    myStr=myStr.replace("b","a").replace("c","a")
    for s in myStr.split("a"):       
        if s!="":
            answer.append(s)
    if len(answer)==0:
        answer= ["EMPTY"]
    return answer