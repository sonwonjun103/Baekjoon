N=int(input())

dp=[0]*(N+1)

for i in range(2, N+1):
    #전 숫자보다 1크니까 횟수를 + 해줌
    dp[i]=dp[i-1]+1
    
    if i%3==0:
        #나눠지면 횟수가 증가하므로 + 해주는데 안해주는 것보다 작으면 뒤에꺼 아니면 앞에꺼
        dp[i]=min(dp[i], dp[i//3]+1)
        
    if i%2==0:
        dp[i]=min(dp[i], dp[i//2]+1)

print(dp[N])