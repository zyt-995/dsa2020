from collections import deque
def topo(adj):
    degree=[0]*len(adj)
    for i in adj:
        for j in i:
            degree[j]+=1
    queue=deque()
    for i in range(len(degree)):
        if degree[i]==0:
            queue.append(i)
    topoorder=[]
    while queue:
        k=queue.popleft()
        topoorder.append(k)
        for i in adj[k]:
            degree[i]-=1
            if degree[i]==0:
                queue.append(i)
    return len(topoorder)!=len(adj)
n,m=map(int,input().split())
adj=[[] for i in range(n)]
for i in range(m):
    u,v=map(int,input().split())
    adj[u].append(v)
if topo(adj):
    print('yes')
else:
    print('no')