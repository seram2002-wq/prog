def solution(my_string):
    target = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    return [my_string.count(char) for char in target]