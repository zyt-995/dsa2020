from collections import deque
n,m=map(int,input().split())
adj=[[] for i in range(n)]
for i in range(m):
    u,v=map(int,input().split())
    adj[u].append(v)
    adj[v].append(u)
q=deque([0])
visited=[False]*n
visited[0]=True
count=1
while q:
    curr=q.popleft()
    for i in adj[curr]:
        if visited[i]==False:
            visited[i]=True
            count+=1
            q.append(i)
if count==n:
    print('connected:yes')
else:
    print('connected:no')
cvisited=[False]*n
def dfs(u,parent):
    cvisited[u]=True
    for v in adj[u]:
        if cvisited[v]==False:
            if dfs(v,u):
                return True
        elif v!=parent:
            return True
    return False
flag=False
for i in range(n):
    if not cvisited[i]:
        if dfs(i,-1):
           flag=True
           print('loop:yes')
           break
if not flag:
    print('loop:no')
#并查集
from collections import deque
n,m=map(int,input().split())
adj=[[] for i in range(n)]
for i in range(m):
    u,v=map(int,input().split())
    adj[u].append(v)
    adj[v].append(u)
q=deque([0])
visited=[False]*n
visited[0]=True
count=1
while q:
    curr=q.popleft()
    for i in adj[curr]:
        if visited[i]==False:
            visited[i]=True
            count+=1
            q.append(i)
if count==n:
    print('connected:yes')
else:
    print('connected:no')
cvisited=[False]*n
def dfs(u,parent):
    cvisited[u]=True
    for v in adj[u]:
        if cvisited[v]==False:
            if dfs(v,u):
                return True
        elif v!=parent:
            return True
    return False
flag=False
for i in range(n):
    if not cvisited[i]:
        if dfs(i,-1):
           flag=True
           print('loop:yes')
           break
if not flag:
    print('loop:no')

