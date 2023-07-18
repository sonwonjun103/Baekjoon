# 1  7 19 37

n=int(input())

result=1
cnt=1

while n > result:
    result += 6 *cnt
    cnt+=1

print(cnt)