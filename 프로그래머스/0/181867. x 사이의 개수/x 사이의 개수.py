def solution(myString):
    answer = []
    x_indices = [i for i, char in enumerate(myString) if char == "x"]
    answer.append(x_indices[0])
    for n in range(len(x_indices)-1):
        answer.append(int(x_indices[n+1])-int(x_indices[n])-1)
    answer.append(len(myString)-x_indices[-1]-1)
    return answer