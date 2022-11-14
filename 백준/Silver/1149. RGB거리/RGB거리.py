N=int(input())
DP=[]
for _ in range(N):
    DP.append(list(map(int, input().split())))
for i in range(1,len(DP)):
    #첫번째 빨
    DP[i][0]=min(DP[i-1][1], DP[i-1][2])+DP[i][0]
    #초
    DP[i][1]=min(DP[i-1][0], DP[i-1][2])+DP[i][1]
    #파
    DP[i][2]=min(DP[i-1][0], DP[i-1][1])+DP[i][2]
print(min(DP[N-1][0], DP[N-1][1], DP[N-1][2]))