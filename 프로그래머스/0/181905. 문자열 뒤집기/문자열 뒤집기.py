def solution(my_string, s, e):
    answer = ''
    r=my_string[s:e+1][::-1]
    answer=my_string[:s]+r+my_string[e+1:]
    return answer