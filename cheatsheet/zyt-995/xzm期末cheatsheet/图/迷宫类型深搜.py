def begin(s,r,c):
    for i in range(r):
        for j in range(c):
            if s[i][j]=='S':
                return i,j
def migong(s,b,e):#深搜的标准过程
    visited=[[False for _ in range(len(s[0]))] for _ in range(len(s))]
    direction=[(0,1),(0,-1),(1,0),(-1,0)]
    best=0
    path=0
    def help(b,e):
        nonlocal best,path#一定要全局化变量（如果是指针类型不用全局化，但是变量类型要全局化）
        path=path+1
        if s[b][e]=='E':
            if best==0 or best>path:
                best=path
            path=path-1
            return
        visited[b][e]=True
        if best!=0 and best<=path:
            visited[b][e]=False
            path=path-1
            return
        for dx,dy in direction:
            bn=dx+b
            en=dy+e
            if 0<=bn<len(s) and 0<=en<len(s[0]):
                if visited[bn][en]==False and (s[bn][en]=='.'or s[bn][en]=='E'):
                    help(bn,en)
        visited[b][e]=False
        path=path-1
    help(b,e)
    return best
a=int(input())
for _ in range(a):
    r,c=map(int,input().split())
    s=[]
    for _ in range(r):
        s.append(input())
    b,e=begin(s,r,c)
    answer=migong(s,b,e)
    if answer==0:
        print('oop!')
    else:
        print(answer-1)
