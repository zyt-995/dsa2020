T=int(input())
for _ in range(T):
    n,m=map(int,input().split())
    head=list(range(n+1))#直接记录所有元素的队首
    for _ in range(m):
        x,y=map(int,input().split())
        hx=x
        while head[hx]!=hx:#只有队首的元素是相等的，也就是队首就是自己本身
            hx=head[hx]#不断迭代找到队首
        hy=y
        while head[hy]!=hy:
            hy=head[hy]
        if hx!=hy:#注意本质上就是在模拟整个过程
            head[hx]=hy#把队首元素直接加到hy上
    for i in range(1,n+1):
        h=i
        while head[h]!=h:
            h=head[h]#找到队首
        head[i]=h
    head.pop(0)
    for j in range(len(head)):
        head[j]=str(head[j])
    print(' '.join(head))