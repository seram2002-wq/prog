def solution(myString):
    myString=list(myString)
    for i in range(len(myString)):
        if myString[i]=="a" or myString[i]=="A":
            myString[i]="A"
        else:
            myString[i]=myString[i].lower()
    return "".join(myString)

