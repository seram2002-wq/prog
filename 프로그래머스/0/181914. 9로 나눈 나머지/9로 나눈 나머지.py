def solution(number):
    answer = 0
    total=sum(int(char) for char in number)
    answer+=total%9
    return answer