'''
250407:求逆序对数
查看提交统计提问
总时间限制: 500ms 内存限制: 65536kB
描述
对于一个长度为N的整数序列A，满足i < j 且 Ai > Aj.的数对(i,j)称为整数序列A的一个逆序

请求出整数序列A的所有逆序对个数

输入
输入包含多组测试数据，每组测试数据有两行
第一行为整数N(1 <= N <= 20000)，当输入0时结束
第二行为N个整数，表示长为N的整数序列
输出
每组数据对应一行，输出逆序对的个数
样例输入
5
1 2 3 4 5
5
5 4 3 2 1
1
1
0
样例输出
0
10
0

'''

def Merge(alist):
    if len(alist)<=1:
        return alist
    else:
        mid=len(alist)//2
        lef_list=Merge(alist[:mid])
        rig_list=Merge(alist[mid:])
        return SortMerge(lef_list,rig_list)

swap_time=0
def SortMerge(lef,rig):
    global swap_time
    ans=[]
    m=len(lef)
    n=len(rig)
    i=0
    j=0
    while True:
        if i==m:
            ans+=rig[j:]
            break
        elif j==n:
            ans+=lef[i:]
            break
        else:
            if lef[i]<=rig[j]:
                ans+=[lef[i]]
                i+=1
            else:
                ans+=[rig[j]]
                j+=1
                swap_time+=m-i
    return ans





while True:
    N=int(input())
    if N==0:
        break
    sequence=list(map(int,input().split()))
    swap_time=0
    Merge(sequence)
    print(swap_time)