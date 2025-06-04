#本题目是寻找最小的最大值，同时答案具有单调性，也就是如果小的不行，那更小的肯定不行。这类题目可以拿二分查找去做
#这时一类二分查找题目的标准格式，也就是维护一个best，之后通过不断的试验去看看这个行不行
n,m=map(int,input().split())
a=[]
for _ in range(n):
    a.append(int(input()))
def exa(a,m,num):
    l=len(a)
    sum=0
    flag=1
    for i in range(l):#一定注意要使用if=elif-else格式，否则可能会多次处理，这个一定要很谨慎
        if sum+a[i]<num:
            sum=sum+a[i]
        elif sum+a[i]>num:
            sum=a[i]
            flag+=1
        else:
            sum=0
            flag+=1
    if flag<=m:
        return True
    else:
        return False
left=max(a)
right=sum(a)
best=0
while left<=right:
    mid=(left+right)//2
    if not exa(a,m,mid):
        left=mid+1
    else:
        best=mid
        right=mid-1
print(best)