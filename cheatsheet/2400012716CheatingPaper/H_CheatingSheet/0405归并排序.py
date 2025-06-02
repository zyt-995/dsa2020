#Freda的越野跑
'''
描述
Freda报名参加了学校的越野跑。越野跑共有N人参加，在一条笔直的道路上进行。这N个人在起点处站成一列，相邻两个人之间保持一定的间距。比赛开始后，这N个人同时沿着道路向相同的方向跑去。换句话说，这N个人可以看作x轴上的N个点，在比赛开始后，它们同时向x轴正方向移动。
假设越野跑的距离足够远，这N个人的速度各不相同且保持匀速运动，那么会有多少对参赛者之间发生“赶超”的事件呢？

输入
第一行1个整数N。
第二行为N 个非负整数，按从前到后的顺序给出每个人的跑步速度。
对于50%的数据，2<=N<=1000。
对于100%的数据，2<=N<=100000。
输出
一个整数，表示有多少对参赛者之间发生赶超事件。
样例输入
5
1 3 10 8 5
样例输出
7
提示
我们把这5个人依次编号为A,B,C,D,E，速度分别为1,3,10,8,5。
在跑步过程中：
B,C,D,E均会超过A，因为他们的速度都比A快；
C,D,E都会超过B，因为他们的速度都比B快；
C,D,E之间不会发生赶超，因为速度快的起跑时就在前边。
'''
def Merge(alist):
    if len(alist)<=1:
        return alist
    else:
        mid=len(alist)//2
        left_list=Merge(alist[:mid])
        right_list=Merge(alist[mid:])
        return SortMerge(left_list,right_list)

time_swap=0
def SortMerge(lef,rig):
    global time_swap
    res=[]
    m=len(lef)
    n=len(rig)
    i=0
    j=0
    while True:
        if i==m:
            res+=rig[j:]
            break
        elif j==n:
            res+=lef[i:]
            break
        else:
            if lef[i]>=rig[j]:
                res.append(lef[i])
                i+=1
            else:
                res.append(rig[j])
                j+=1
                time_swap+=m-i
    return res
        

N=int(input())

speeds=list(map(int,input().split()))
time_swap=0
Merge(speeds)
print(time_swap)
















'''
N=int(input())
speeds=list(map(int,input().split()))
fast_speed=max(speeds)
record_of_speeds=[0]*(fast_speed+1)
events=0
for i in range(N):
    events+=record_of_speeds[speeds[i]]
    for t in range(speeds[i]+1,fast_speed+1):
        record_of_speeds[t]+=1
print(events)
'''


