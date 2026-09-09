def solution(myString, pat):
    answer = 0
    num=myString.find(pat)
    while num!=-1:
        myString=myString[num+1:]
        answer+=1
        num=myString.find(pat)

    return answer