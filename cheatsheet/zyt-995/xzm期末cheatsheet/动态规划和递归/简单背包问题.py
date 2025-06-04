while True:
    n,k=map(int,input().split())
    if n==0 and k==0:
        break
    a=list(map(int,input().split()))
    dp=[[0 for _ in range(k)]for _ in range(n+1)]
    dp[0][0]=1
    for i in range(1,k):
        for j in range(1,n+1):
            if j>=a[i]:
                dp[j][i]=dp[j][i-1]+dp[j-a[i]][i-1]
            elif j<a[i]:
                dp[j][i]=dp[j][i-1]
    print(dp)
    print(dp[n][k-1])
