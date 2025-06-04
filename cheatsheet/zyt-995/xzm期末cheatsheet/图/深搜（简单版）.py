n,m=map(int,input().split())
g=[[]for _ in range(n)]
visited=[False]*(n)
def shensou(k,g):
    path=[]
    def help(k):
        path.append(k)
        visited[k]=True
        for next in g[k]:
            if not visited[next]:
                help(next)
    help(k)
    return path
for _ in range(m):
    a,b=map(int,input().split())
    g[a].append(b)
    g[b].append(a)
for i in range(n):
    g[i].sort()
result=[]
for i in range(n):
    if not visited[i]:
        result+=shensou(i,g)
for j in range(n):
    result[j]=str(result[j])
print(' '.join(result))
