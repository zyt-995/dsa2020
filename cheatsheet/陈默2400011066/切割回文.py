def min_cut(s):
    n = len(s)
    if n == 0:
        return 0
    # 预处理回文数组
    isPal = [[False] * n for _ in range(n)]
    for i in range(n):
        isPal[i][i] = True
    for i in range(n-1):
        if s[i] == s[i+1]:
            isPal[i][i+1] = True
    for l in range(3, n+1):
        for i in range(n - l + 1):
            j = i + l - 1
            if s[i] == s[j] and isPal[i+1][j-1]:
                isPal[i][j] = True
    # 动态规划
    dp = [float('inf')] * (n + 1)
    dp[0] = -1  # 初始条件，0个字符需要-1次切割
    for i in range(1, n+1):
        for j in range(i):
            if isPal[j][i-1]:
                if dp[j] + 1 < dp[i]:
                    dp[i] = dp[j] + 1
    return dp[n]

def main():
    import sys
    T = int(sys.stdin.readline())
    for _ in range(T):
        s = sys.stdin.readline().strip()
        print(min_cut(s))

if __name__ == "__main__":
    main()