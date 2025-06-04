#并查集常常用于图算法，是这种数据类型很好的总结。
#以作弊问题为例题。应用广搜
n,m=map(int,input().split())
g=[[]for _ in range(n+1)]#创建邻接表
for _ in range(m):
    a,b=map(int,input().split())
    g[a].append(b)
    g[b].append(a)#注意这是无向图
visited=[None]*(n+1)
def guangsou(x):#使用广搜方法，把所有作弊的同学进行标记.这是广搜的经典做法
    q=[]
    q.append(x)
    visited[x]=True
    while q:
        now=q.pop(0)
        for next in g[now]:
            if not visited[next]:
                visited[next]=True
                q.append(next)
    return 1
num=0
for i in range(1,n+1):#以下进行并查集的操作，也就是看有多少连通的图
    if not visited[i]:
        guangsou(i)
        num=num+1
print(num)
