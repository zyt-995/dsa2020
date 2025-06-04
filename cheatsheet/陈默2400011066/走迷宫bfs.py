from collections import deque
n,m=map(int,input().split())
maze=[]
for i in range(n):
    maze.append(input())
q=deque([(0,0)])
visited=set()
visited.add((0,0))
find=False
dire=[(-1,0),(0,-1),(1,0),(0,1)]
while q:
    x,y=q.popleft()
    if x==n-1 and y==m-1:
        print(1)
        find=True
        break
    for dx,dy in dire:
        nx,ny=x+dx,y+dy
        if 0<=nx<n and 0<=ny<m and maze[nx][ny]=='.' and (nx,ny) not in visited:
            q.append((nx,ny))
            visited.add((nx,ny))
if not find:
    print(0)


