def solution(date1, date2):
    answer = 0
    data01=date1[0]*10000+date1[1]*100+date1[2]
    data02=date2[0]*10000+date2[1]*100+date2[2]
    if data01<data02:
        answer+=1
    return answer