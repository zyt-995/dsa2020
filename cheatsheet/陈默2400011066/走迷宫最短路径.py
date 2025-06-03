from collections import deque
def path():
    n,m=map(int,input().split())
    maze=[]
    for i in range(n):
        a=list(input().strip())
        maze.append(a)
    visited=[[False]*m for i in range(n)]
    queue=deque([(0,0,[(0,0)])])
    visited[0][0]=True
    while queue:
        x,y,path=queue.popleft()
        if x==n-1 and y==m-1:
            return path
        for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            nx,ny=x+dx,y+dy
            if 0<=nx<n and 0<=ny<m:
                if not visited[nx][ny] and maze[nx][ny]==".":
                    visited[nx][ny]=True
                    new_path=path+[(nx,ny)]
                    queue.append((nx,ny,new_path))
    return None
path=path()
if path:
    print(''.join(f'({x},{y})' for x, y in path))
else:
    print(0)
