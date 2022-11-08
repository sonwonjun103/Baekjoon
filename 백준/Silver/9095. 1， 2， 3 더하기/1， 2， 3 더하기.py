N=int(input())

def check(N):
    dp=[]
    dp.append(1)
    dp.append(2)
    dp.append(4)
    
    if N==1:
        return 1
    elif N==2:
        return 2
    elif N==3:
        return 4
    else:
        for i in range(3, N):
            dp.append(sum(dp[i-3:i]))
            
    return dp[N-1]

for i in range(N):
    n=int(input())
    print(check(n))