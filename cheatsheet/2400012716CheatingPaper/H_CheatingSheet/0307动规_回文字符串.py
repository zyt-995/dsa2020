'''
250307:回文字符串
查看提交统计提问
总时间限制: 10000ms 单个测试点时间限制: 1000ms 内存限制: 262144kB
描述
给定一个字符串 S ，最少需要几次增删改操作可以把 S 变成一个回文字符串？

一次操作可以在任意位置插入一个字符，或者删除任意一个字符，或者把任意一个字符修改成任意其他字符。

输入
字符串 S。S 的长度不超过100, 只包含'A'-'Z'。
输出
最少的修改次数。
样例输入
ABAD
样例输出
1
'''

def min_change(s):
    n=len(s)
    dp=[[0]*n for _ in range(n)]
    for l in range(2,n+1):
        for i in range(n-l+1):
            j=i+l-1
            if s[i]==s[j]:
                dp[i][j]=dp[i+1][j-1]
            else:
                dp[i][j]=min(dp[i+1][j]+1,dp[i][j-1]+1,dp[i+1][j-1]+1)
    return dp[0][n-1]



s=list(input())
print(min_change(s))











"""
str0=list(input())
left_point=0
right_point=len(str0)-1
min_change=len(str0)

def improve_string(le,ri,s,change):
    global min_change
    if change>=min_change:
        return
    if le==ri:
        min_change=min(min_change,change)
        return
    if le+1==ri:
        if s[le]==s[ri]:
            min_change=min(min_change,change)
            return
        else:
            min_change=min(min_change,change+1)
            return
    if s[le]!=s[ri]:
#        s1=[item for item in s]
#        s2=[item for item in s]
#        s3=[item for item in s]
#        s1.pop(le)
#        s2.pop(ri)
#        s3[le]=s3[ri]
        improve_string(le+1,ri,s,change+1)
        improve_string(le,ri-1,s,change+1)
        improve_string(le+1,ri-1,s,change+1)
    else:
#        s1=copy.deepcopy(s)
#        s2=copy.deepcopy(s)
#        s3=copy.deepcopy(s)
        improve_string(le+1,ri-1,s,change)
#        s2.pop(le)
#        s3.pop(ri)
#        improve_string(le,ri-1,s2,change+1)
#        improve_string(le,ri-1,s3,change+1)

improve_string(left_point,right_point,str0,0)
print(min_change)
"""