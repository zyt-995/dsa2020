from collections import deque
n,k=map(int,input().split())
if n>=k:
    print(n-k)
else:
    visited=[False]*100001
    visited[n]=True
    queue=deque()
    queue.append((n,0))
    visited[n]=True
    mintime=float('inf')
    while queue:
        loc,time=queue.popleft()
        if loc==k:
            mintime=min(mintime,time)
            break
        if loc >k:
            poss=time+(loc-k)
            if poss<mintime:
                mintime=poss
            continue
        for a1 in [loc+1,loc-1,2*loc]:
            if 100001>=a1>=0 and not visited[a1]:
                   visited[a1]=True
                   queue.append((a1,time+1))
    print(mintime)