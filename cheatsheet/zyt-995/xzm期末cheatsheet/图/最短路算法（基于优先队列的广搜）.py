import heapq
class Node:
    def __init__(self,r,c,value):
        self.r=r
        self.c=c
        self.value=value
    def __lt__(self,other):#为了使用heapq的优先队列，需要定义一个比大小
        return self.value<other.value
def start(s,hang,lie):
    for i in range(hang):
        for j in range(lie):
            if s[i][j]=='r':
                return i,j
def guangsou(s,r,c):#普通的广搜不行，因为需要考虑到每一轮扩散都是等时间的，但是由于有守卫的存在，所以做不到等时间
    direction=[(0,1),(0,-1),(1,0),(-1,0)]
    hang=len(s)#用形象化的思维去思考行列到底对应哪个
    lie=len(s[0])
    visited=[[float('inf') for _ in range(lie)]for _ in range(hang)]
    q=[]
    heapq.heappush(q,Node(r,c,0))
    visited[r][c]=0
    while len(q)>0:
        now=heapq.heappop(q)
        if s[now.r][now.c]=='a':
            return now.value
        else:
            for dx,dy in direction:
                x=dx+now.r
                y=dy+now.c
                if 0<=x<hang and 0<=y<lie and s[x][y]!='#':
                    if s[x][y]=='@' or s[x][y]=='a':#一定要记住这里面加上到达终点的情况，否则永远都不会试探终点的情况，好好想想这个逻辑
                        now_value=now.value+1
                    elif s[x][y]=='x':
                        now_value=now.value+2
                    if now_value<visited[x][y]:#只有更小的才有资格入队
                        visited[x][y]=now_value
                        heapq.heappush(q,Node(x,y,now_value))
    return -1
n=int(input())
for _ in range(n):
    hang,lie=map(int,input().split())
    s=[]
    for _ in range(hang):
        s.append(input())
    r,c=start(s,hang,lie)
    answer=guangsou(s,r,c)
    if answer==-1:
        print('Impossible')
    else:
        print(answer)