'''
250301:简单的整数划分问题
查看提交统计提问
总时间限制: 100ms 内存限制: 65536kB
描述
将正整数n 表示成一系列正整数之和，n=n1+n2+…+nk, 其中n1>=n2>=…>=nk>=1 ，k>=1 。
正整数n 的这种表示称为正整数n 的划分。正整数n 的不同的划分个数称为正整数n 的划分数。

输入
标准的输入包含若干组测试数据。每组测试数据是一个整数N(0 < N <= 50)。
输出
对于每组测试数据，输出N的划分数。
样例输入
5
样例输出
7
提示
5, 4+1, 3+2, 3+1+1, 2+2+1, 2+1+1+1, 1+1+1+1+1
'''


from functools import lru_cache
@lru_cache(maxsize=None)
def divide(n,x):#n reprsents the current num while x limits the next slice
    if x==1:
        return 1
    elif n==0:
        return 1
    else:
        sum=0
        for i in range(1,min(x+1,n+1)):
            sum+=divide(n-i,i)
        return sum

try:
    while True:
        item=int(input())
        print(divide(int(item),int(item)))
except:
    pass

'''
import sys
for item in sys.stdin:
    print(divide(int(item),int(item)))'
'''