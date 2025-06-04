n,m=map(int,input().split())
def dfs(r,c,g):
    visited=[[False for _ in range(m)] for _ in range(n)]
    path=[]
    best=[]
    directions=[(1,0),(-1,0),(0,1),(0,-1)]
    def help(r,c):
        path.append((r,c))
        if r==n-1 and c==m-1:
            if len(best)==0 or len(best)>len(path):
                best[:]=path[:]#python里面直接b=a是指针传递，使用切片就是我们想要的样子
                path.pop()
                return 
        if len(best)!=0 and len(path)>=len(best):
            path.pop()
            return 
        visited[r][c]=True
        for dx,dy in directions:
            rn=r+dx
            cn=c+dy
            if 0<=rn<n and 0<=cn<m and visited[rn][cn]==False and g[rn][cn]=='.':
                help(rn,cn)
        visited[r][c]=False
        path.pop()
    help(r,c)
    return best
g=[]
for i in range(n):
    g.append(input())
answer=dfs(0,0,g)
if answer==[]:
    print(0)
else:
    result=[]
    for x,y in answer:
        s=f'({x},{y})'
        result.append(s)

    print(''.join(result))