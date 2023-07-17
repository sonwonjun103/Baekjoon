n=int(input())

for i in range(1, n+1):
    num="{}".format(i)
    cnt=0
    for s in num:
        cnt+=int(s)

    cnt+=i

    if cnt==n:
        print(i)
        break

    if i==n:
        print(0)