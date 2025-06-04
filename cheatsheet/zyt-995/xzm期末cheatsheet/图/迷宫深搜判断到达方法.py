n,m=map(int,input().split())
def bfs(r,c,g):
    visited=[[False for _ in range(m)] for _ in range(n)]
    direction=[(-1,0),(1,0),(0,1),(0,-1)]
    def help(r,c):
        if r==n-1 and c==m-1:
            return 1
        visited[r][c]=True
        total=0
        for dx,dy in direction:
            rn,cn=r+dx,c+dy
            if 0<=rn<n and 0<=cn<m:
                if visited[rn][cn]==False and g[rn][cn]=='.':
                    total=total+help(rn,cn)
        visited[r][c]=False#考虑到需要多条路径，因此回溯
        return total
    return help(r,c)
g=[]
for i in range(n):
    g.append(input())
print(bfs(0,0,g))