n,c=map(int,input().split())
alist=[int(input()) for i in range(n)]
alist.sort()
def canplace(k):
    flag=0
    count=1
    for i in range(1,n):
        if alist[i]-alist[flag]>=k:
            count+=1
            flag=i
    return count>=c
left=0
right=alist[-1]-alist[0]
while left<right:
    mid=(left+right+1)//2
    if canplace(mid):
        left=mid
    else:
        right=mid-1
print(left)
