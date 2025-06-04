while True:
    try:
        n,k=map(int,input().split())
        dp1 = [[0] * (k + 1) for _ in range(n + 1)]
        dp1[0][0] = 1  # 初始化：0划分为0个正整数的方案数为1
            
        for i in range(1, n + 1):
            for j in range(1, k + 1):
                if i < j:
                    dp1[i][j] = 0  # 无法划分
                else:
                    dp1[i][j] = dp1[i - 1][j - 1] + dp1[i - j][j]
            
        print(dp1[n][k])
        dp2=[0]*(n+1)
        dp2[0]=1
        for p in range(1,n+1):
            for q in range(n,p-1,-1):
                dp2[q]+=dp2[q-p]
        print(dp2[n])
        dp3=[0]*(n+1)
        dp3[0]=1
        for x in range(1,n+1,2):
            for y in range(x,n+1):
                dp3[y]+=dp3[y-x]
        print(dp3[n])
    except:
        break