n,m=map(int,input().split())
visited=[[False]*m for _ in range(n)]
maze=[]
for i in range(n):
    maze.append(input())
count=0
dire=[(-1,0),(1,0),(0,-1),(0,1)]
def dfs(i,j):
    global count
    if i==n-1 and j==m-1:
        count+=1
    visited[i][j]=True
    for dx,dy in dire:
        nx,ny=i+dx,j+dy
        if 0<=nx<n and 0<=ny<m and maze[nx][ny]=='.' and visited[nx][ny]==False:
            dfs(nx,ny)
    visited[i][j]=False
dfs(0,0)
print(count)

