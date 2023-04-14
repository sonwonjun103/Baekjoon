def solution(order):
    q=[]
    index=1
    want=0
    while index!=len(order)+1:
        q.append(index)
        while q[-1]==order[want]:
            want+=1
            q.pop()
            
            if len(q) == 0:
                break
        index+=1
    return want