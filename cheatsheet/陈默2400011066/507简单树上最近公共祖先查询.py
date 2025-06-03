from collections import deque
N,R=map(int,input().split())
parent=[0]*(N+1)
adj=[[] for _ in range(N+1)]
for i in range(N-1):
    u,v=map(int,input().split())
    adj[u].append(v)
    adj[v].append(u)
depth=[0]*(N+1)
queue=deque()
queue.append(R)
visited=[False]*(N+1)
visited[R]=True
while queue:
    curr=queue.popleft()
    for i in adj[curr]:
        if not visited[i] and i!=parent[curr]:
            parent[i]=curr
            depth[i]+=depth[curr]+1
            visited[i]=True
            queue.append(i)
Q=int(input())
for i in range(Q):
    x, y = map(int, input().split())
    a, b = x, y
    while depth[a] > depth[b]:
        a = parent[a]
    while depth[b] > depth[a]:  # 把a,b调整到同一深度
        b = parent[b]
    while a != b:
        a = parent[a]
        b = parent[b]
    print(a)
