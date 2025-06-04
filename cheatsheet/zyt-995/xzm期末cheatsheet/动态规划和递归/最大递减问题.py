#这是一个找寻最大递减的问题，有标准的解法
n = int(input())
a = list(map(int, input().split()))
dp = [[1] for _ in range(n)]  # 初始化每个位置的击落数都为1
#其核心要义在于选择位置i，之后历遍前面的所有的导弹，如果更高的话就可以加上。不高的话就不能加上，就不理了。之后最后输出这个dp的最大值
for i in range(1, n):
    for j in range(i):
        if a[j] >= a[i]:
            dp[i][0] = max(dp[i][0], dp[j][0] + 1)
print(max([row[0] for row in dp]))