n=int(input())
a=list(map(int, input().split()))

cnt=0
for i in a:
    if i!=1:
        check=0
        for j in range(2, i):
            if i%j==0:
                check=1
                break
                
        if check==0:
            cnt+=1

print(cnt) 