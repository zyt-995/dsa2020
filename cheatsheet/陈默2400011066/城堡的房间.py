from collections import deque

r,c=map(int,input().split())
castle=[]
for i in range(r):
    s=input()
    castle.append(s)
count=0
s=0
visited=[[False]*c for _ in range(r)]
dire=[(-1,0),(0,1),(1,0),(0,-1)]
for i in range(r):
    for j in range(c):
        if castle[i][j]=="." and not visited[i][j]:
            visited[i][j] = True
            queue=deque([(i,j)])
            currsize=1
            count+=1
            while queue:
                x,y=queue.popleft()
                for dx,dy in dire:
                    nx,ny=x+dx,y+dy
                    if 0<=nx<r and 0<=ny<c and visited[nx][ny]==False and castle[nx][ny]==".":
                        visited[nx][ny]=True
                        currsize+=1
                        queue.append((nx,ny))
            if currsize>s:
                s=currsize
print(count)
print(s)

