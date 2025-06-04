n,m=map(int,input().split())
visited=[False]*n
result=[]
def dfs(u,adj):
    visited[u]=True
    result.append(u)
    for i in adj[u]:
        if not visited[i]:
            dfs(i,adj)
adj=[[] for i in range(n)]
for i in range(m):
    a,b=map(int,input().split())
    adj[a].append(b)
    adj[b].append(a)
for i in range(n):
    if not visited[i]:
        dfs(i,adj)
print(" ".join(map(str,result)))