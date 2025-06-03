from collections import deque
n,r=map(int,input().split())
adj=[[] for i in range(n+1)]
for i in range(n-1):
    u,v=map(int,input().split())
    adj[u].append(v)
    adj[v].append(u)
dep=[0]*(n+1)
queue=deque([(r,0)])
visited=set()
visited.add(r)
parent=[0]*(n+1)
while queue:
    node,depth=queue.popleft()
    for neighbor in adj[node]:
        if neighbor not in visited:
            queue.append((neighbor,depth+1))
            dep[neighbor]=depth+1
            parent[neighbor]=node
            visited.add(neighbor)
def findpa(m,n):
    if dep[m]<dep[n]:
        m,n=n,m
    if dep[m]>dep[n]:
        return findpa(parent[m],n)
    if dep[m]==dep[n]:
         if m==n:
             return m
         if parent[m]==parent[n]:
            return parent[m]
         else:
             return findpa(parent[m],parent[n])
q=int(input())
for i in range(q):
    x,y=map(int,input().split())
    if findpa(x,y)==0:
        print(r)
    else:
        print(findpa(x,y))





