T=int(input())
def panduan(dis,i,k):
    forbid=dis[i]-k
    if forbid<=0:
        return 0
    else:
        for m in range(i):
            if forbid<=dis[m]:
                return m-1
    return i-1
for _ in range(T):
    n,k=map(int,input().split())
    dis=list(map(int,input().split()))
    dis.insert(0,0)
    value=list(map(int,input().split()))
    value.insert(0,0)
    dp=[0]*(n+1)
    dp[1]=value[1]
    for i in range(2,n+1):
        m=panduan(dis,i,k)
        dp[i]=max(dp[i-1],dp[m]+value[i])
    print(dp[n])

