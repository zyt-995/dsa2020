n,m=map(int,input().split())
adj=[[]for i in range(n)]
for i in range(m):
    a,b=map(int,input().split())
    adj[a].append(b)
    adj[b].append(a)
def dfs():
    visited=set()
    result=[]
    def helper(u):
        nonlocal visited
        nonlocal result
        visited.add(u)
        result.append(u)
        for v in adj[u]:
            if v not in visited:
                helper(v)
    for i in range(n):
        if i not in visited:
            helper(i)
    return result
ans=dfs()
print(" ".join(map(str,ans)))
