#拓扑排序，用于有向无环图。用于确定先后顺序
n,m=map(int,input().split())
g=[[]for _ in range(n)]
level=[0]*n
indegree=[0]*n
for _ in range(m):
    a,b=map(int,input().split())
    g[b].append(a)
    indegree[a]+=1
q=[]
seq=[]
v=0
visited=[False]*n
for i in range(n):
    if indegree[i]==0:
        q.append(i)
        visited[i]=True
while q:
    now=q.pop(0)
    for next in g[now]:
        if not visited[next]:
            indegree[next]-=1
            level[next]=1+level[now]
            if indegree[next]==0:
                q.append(next)
                visited[next]=True
zonghe=sum(level)+n*100
print(zonghe)

            
