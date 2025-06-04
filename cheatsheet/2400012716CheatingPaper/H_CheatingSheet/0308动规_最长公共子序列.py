'''
250308:最长的公共子序列的长度
查看提交统计提问
总时间限制: 1000ms 内存限制: 10240kB
描述
我们称一个字符的数组S为一个序列。对于另外一个字符数组Z,如果满足以下条件，则称Z是S的一个子序列：（1）Z中的每个元素都是S中的元素（2）Z中元素的顺序与在S中的顺序一致。例如：当S = (E,R,C,D,F,A,K)时，（E，C，F）和（E，R）等等都是它的子序列。而（R，E）则不是。

现在我们给定两个序列，求它们最长的公共子序列的长度。

输入
一共两行，分别输入两个序列。
输出
一行，输出最长公共子序列的长度。
样例输入
ABCBDAB

BDCABA
样例输出
4
'''

def longest_shared_chars(s1,s2):
    m=len(s1)
    n=len(s2)
    dp=[[0]*(n+1) for _ in range(m+1)]
    for i in range(1,m+1):
        for j in range(1,n+1):
            if s1[i-1]==s2[j-1]:
                dp[i][j]=dp[i-1][j-1]+1
            else:
                dp[i][j]=max(dp[i-1][j],dp[i][j-1])
    return dp[m][n]

str1=list(input())
str2=list(input())
print(longest_shared_chars(str1,str2))


#思路：将一个序列的长度从1开始，后面新增的字符是前面的字符的或者前面
# 字符+1，对每一个字符长度（字符）需要记录当前最大长度和对应子串的位置
'''
def longest_shared_chars(s1,s2):
    n=len(s2)
    max_shared=[0 for _ in range(n)]
    position=[-1 for _ in range(n)]
    for i in range(n):
        if s2[i] not in s1:
            continue
        else:
            if max(max_shared)==0:
                position[i]=s1.index(s2[i])
                max_shared[i]=1
            else:
                position[i]=s1.index(s2[i])
                max_shared[i]=1
                for j in range(i):
                    if max_shared[j]>=max_shared[i]:
                        if s2[i] in s1[position[j]+1:]:
                            max_shared[i]=max_shared[j]+1
                            position[i]=s1.index(s2[i],position[j]+1)
                        elif max_shared[j]==max_shared[i]:
                            max_shared[i]=max_shared[j]
                            position[i]=min(position[j],position[i])
                    elif max_shared[j]==max_shared[i]-1 and s2[i] in s1[position[j]+1:]:
                        position[i]=min(s1.index(s2[i],position[j]+1),position[i])
                    
    return max(max_shared)

str1=list(input())
str2=list(input())
if len(str1)<len(str2):
    str1,str2=str2,str1
print(longest_shared_chars(str1,str2))

'''