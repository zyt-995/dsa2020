r,c=map(int,input().split())
rows=[]
for i in range(r):
    row=list(map(int,input().split()))
    rows.append(row)
dp=[[1]*c for _ in range(r)]
dire=[(-1,0),(1,0),(0,-1),(0,1)]
visited=[[False]*c for _ in range(r)]
ans=1
def maxpath(i,j):
    global ans
    if not visited[i][j]:
        visited[i][j]=True
        for dx,dy in dire:
            nx,ny=i+dx,j+dy
            if 0<=nx<r and 0<=ny<c and rows[nx][ny]<rows[i][j]:
                if visited[nx][ny]==False:
                    maxpath(nx,ny)
                dp[i][j]=max(dp[i][j],dp[nx][ny]+1)
        if dp[i][j]>ans:
                ans=dp[i][j]
for i in range(r):
    for j in range(c):
        maxpath(i,j)

print(ans)






