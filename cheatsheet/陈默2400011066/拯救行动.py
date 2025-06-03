import heapq
dire=[(1,0),(0,1),(-1,0),(0,-1)]
def dijkstra(maze,start,goal):
    heap=[(0,start)]
    visited = set()
    visited.add(start)
    while heap:
        t,curr=heapq.heappop(heap)
        if curr==goal:
            return t
        for dx,dy in dire:
            nx,ny=curr[0]+dx,curr[1]+dy
            if (nx,ny) not in visited and 0<=nx<len(maze) and 0<=ny<len(maze[0]):
                visited.add((nx,ny))
                if maze[nx][ny]=="a" or maze[nx][ny]=="@":
                    heapq.heappush(heap,(t+1,(nx,ny)))
                if maze[nx][ny]=="x":
                    heapq.heappush(heap,(t+2,(nx,ny)))
    return None
s=int(input())
for i in range(s):
    n,m=map(int,input().split())
    maze=[]
    for _ in range(n):
        s=input()
        maze.append(s)
        if "r" in s:
            start=(_,s.index("r"))
        if "a" in s:
            goal=(_,s.index("a"))
    if dijkstra(maze,start,goal)==None:
        print("Impossible")
    else:
        print(dijkstra(maze,start,goal))