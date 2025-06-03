from collections import deque
dire=[(1,0),(0,1),(-1,0),(0,-1)]
def bfs(maze,start,goal):
    queue = deque([(start,0)])
    visited = set()
    visited.add(start)
    while queue:
          curr,t=queue.popleft()
          if curr==goal:
              return t
          for dx,dy in dire:
              nx,ny=curr[0]+dx,curr[1]+dy
              if 0<=nx<len(maze) and 0<=ny<len(maze[0]):
                  if maze[nx][ny]!="#" and (nx,ny) not in visited:
                      visited.add((nx,ny))
                      queue.append(((nx,ny),t+1))
t=int(input())
for i in range(t):
    r,c=map(int,input().split())
    maze=[]
    for j in range(r):
        s=input()
        maze.append(s)
        if "S" in s:
            start=(j,s.index("S"))
        if "E" in s:
            goal=(j,s.index("E"))
    if bfs(maze,start,goal):
       print(bfs(maze,start,goal))
    else:
        print("oop!")
