#10773번
def pop(stack):
    global top
    if top==-1:
        return
    else:
        data=stack[top]
        stack[top]=0
        top-=1

def push(stack, data, size):
    global top
    if top==size-1:
        return
    else:
        top+=1
        stack[top]=data
top=-1
if __name__=='__main__':
    K=int(input())
    stack=[0 for _ in range(K)]
    for _ in range(K):
        n=int(input())
        if n==0:
            pop(stack)
        else:
            push(stack,n, K)

    print(sum(stack))