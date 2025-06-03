def sep(lst,start,remain,maxspend):
    if remain<=0:
        return
    if len(lst)-start<remain:
        return
    if len(lst)-start==remain:
        return max(maxspend,max(lst[start:]))
    ans=float("inf")
    for i in range(start+1,len(lst)+1):
        curmax=max(maxspend,sum(lst[start:i]))
        if sep(lst,i,remain-1,curmax):
            temp=sep(lst,i,remain-1,curmax)
            if temp<ans:
               ans=temp
    return ans
n,m=map(int,input().split())
spent=[]
for i in range(n):
    a=int(input())
    spent.append(a)
print(sep(spent,0,m,0))

