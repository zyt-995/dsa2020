n=int(input())
values=list(map(int,input().split()))
select=[0]*(n+1)
unselect=[0]*(n+1)
visited=[False]*(n+1)
def dp(i):
    visited[i]=True
    select[i]=values[i-1]
    for k in [2*i,2*i+1]:
        if k<=n:
            if visited[k]==False:
                dp(k)
            unselect[i]+=max(unselect[k],select[k])
            select[i]+=unselect[k]
dp(1)
print(max(select[1],unselect[1]))


