#1003
count0=[1,0,1]
count1=[0,1,1]

def fibonacci(n):
    if len(count0)<=n:
        for i in range(len(count0),n+1):
            count0.append(count0[i-1]+count0[i-2])
            count1.append(count1[i-1]+count1[i-2])

    print(count0[n], count1[n])

N=int(input())
for _ in range(N):
    num=int(input())
    fibonacci(num)