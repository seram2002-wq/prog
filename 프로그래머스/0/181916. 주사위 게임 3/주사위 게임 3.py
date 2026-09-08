def solution(a, b, c, d):
    answer = 0
    dice=sorted([a,b,c,d])
    if dice[0]==dice[3]:
        answer+=dice[0]*1111
    elif dice[0]==dice[2]:
        answer+=(10*dice[0]+dice[3])**2
    elif dice[1]==dice[3]:
        answer+=(10*dice[1]+dice[0])**2
    elif dice[0]==dice[1] and dice[2]==dice[3]:
        answer+=(dice[0]+dice[2])*abs((dice[0]-dice[2]))
    elif dice[0]==dice[1]:
        answer+=dice[2]*dice[3]
    elif dice[1]==dice[2]:
        answer+=dice[0]*dice[3]
    elif dice[0]==dice[2]:
        answer+=dice[1]*dice[3]
    elif dice[0]==dice[3]:
        answer+=dice[2]*dice[1]
    elif dice[2]==dice[3]:
        answer+=dice[0]*dice[1]    
    else:
        answer+=dice[0]
    
    return answer