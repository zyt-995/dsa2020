import heapq
from heapq import heapify

n,m=map(int,input().split())
adj=[[] for _ in range(n+1)]
for i in range(m):
    a,b,c=map(int,input().split())
    adj[a].append((c,b))
q=[(0,1)]
heapq.heapify(q)
dp=[float("inf")]*(n+1)
dp[1]=0
while q:
    length,cur=heapq.heappop(q)
    if length>dp[cur]:
        continue
    for c,b in adj[cur]:
        newcost=length+c
        if newcost<dp[b]:
            dp[b]=newcost
            heapq.heappush(q,(newcost,b))
print(dp[n])


