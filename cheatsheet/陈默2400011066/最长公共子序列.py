s1=input().strip()
s2=input().strip()
l1=len(s1)
l2=len(s2)
dp=[[0]*(l1+1) for i in range(l2+1)]
for i in range(l1):
    for j in range(l2):
        if s1[i]==s2[j]:
            dp[j+1][i+1]=dp[j][i]+1
        else:
            dp[j+1][i+1]=max(dp[j][i+1], dp[j+1][i])
print(dp[-1][-1])