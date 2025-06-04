n,m=map(int,input().split())
def bfs(r,c,g):
    
    visited=[[False for _ in range(m)] for _ in range(n)]
    direction=[(-1,0),(1,0),(0,1),(0,-1)]
    def help(r,c):
        if r==n-1 and c==m-1:
            return 1
        visited[r][c]=True
        for u in direction:
            r_new=r+u[0]
            c_new=c+u[1]
            if 0<=r_new<n and 0<=c_new<m:
                if visited[r_new][c_new]==False and g[r_new][c_new]=='.':
                    if help(r_new,c_new)==1:
                        return 1
        return 0
    return help(r,c)
g=[]
for i in range(n):
    g.append(input())
print(bfs(0,0,g))