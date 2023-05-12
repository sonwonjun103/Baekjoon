def solution(want, number, discount):
    answer = 0
    l=len(discount)
    people=dict()
    for i in range(len(want)):
        people[want[i]]=number[i]

    for day in range(0, l-10+1):
        discount10=discount[day:day+10]
        temp=0
        for w in want:
            if people[w]!=discount10.count(w):
                temp=1
        if temp==0:
            answer+=1
        
    return answer