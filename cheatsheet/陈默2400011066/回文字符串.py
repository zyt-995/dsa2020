s=input().strip()
dp=[[0]*len(s) for i in range(len(s))]
for i in range(len(s)-2,-1,-1):#倒序遍历
    for j in range(i+1,len(s)):
        if s[i]==s[j]:
            if j!=i+1:
                dp[i][j]=dp[i+1][j-1]
        else:
            if j != i + 1:
                 delete=min(dp[i+1][j]+1,dp[i][j-1]+1)
                 modify=dp[i+1][j-1]+1
                 dp[i][j]=min(delete,modify)
            else:
                dp[i][j]=1
print(dp[0][-1])