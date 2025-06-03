def sep(lst,k):
    ans=0
    for l,r,w,h in lst:
        if r<=k:
            ans+=w*h
        elif l>=k:
            ans-=w*h
        else:
            ans+=(2*k-l-r)*h
    return ans
r=int(input())
num=int(input())
lst=[]
start=0
end=r
for i in range(num):
    l,t,w,h=map(int,input().split())
    lst.append((l,l+w,w,h))
while start<=end:
    mid=(start+end)//2
    if sep(lst,mid)==0:
        break
    elif sep(lst,mid)<0:
        start=mid+1
    else:
        end=mid-1
ans=mid
while ans+1<=r and sep(lst,ans)==sep(lst,ans+1):
    ans+=1
print(ans)