from collections import deque
dire=[(-1,0),(1,0),(0,-1),(0,1)]
def findisland(lst):
    island=set()
    queue
    def bfs(start):

        for dx,dy in dire:
            nx,ny=dx+start[0],dy+start[1]
            if 0<=nx<len(lst) and 0<=ny<len(lst[0]):
                if lst[nx][ny]=='1' and (nx,ny) not in island:
                    island.add((nx,ny))
                    queue.append((nx,ny))
    found=False
    for i in range(len(lst)):
        for j in range(len(lst[0])):
            if lst[i][j]=='1':
                bfs((i,j))
                found=True
                break
        if found:break
#不要分开对每一个点bfs，用多源bfs
    visited=set(island)
    queue=deque()
    for (x,y) in visited:
        queue.append((x,y,0))
    while queue:
        x,y,l=queue.popleft()
        for dx,dy in dire:
            nx,ny=x+dx,y+dy
            if 0<=nx<len(lst) and 0<=ny<len(lst[0]):
                if lst[nx][ny]=='1' and (nx,ny) not in visited:
                    return l
                visited.add((nx,ny))
                queue.append((nx,ny,l+1))
n=int(input())
maplist=[]
for i in range(n):
    s=input()
    maplist.append(s)
final=findisland(maplist)
print(final)






