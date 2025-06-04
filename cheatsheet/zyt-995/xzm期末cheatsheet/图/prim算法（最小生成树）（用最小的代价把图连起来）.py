import heapq
n=int(input())
class Edge:
    def __init__(self,c,value):
        self.c=c
        self.value=value
    def __lt__(self,other):
        return self.value<other.value
class Node:
    def __init__(self,name,prev=None,dist=float('inf')):#这里面dist的意义是距离已被扩展的点的最近距离
        self.name=name
        self.prev=prev
        self.dist=dist
    def __lt__(self,other):
        return self.dist<other.dist
def prim(g,r):#g记录了所有的node对应的edge
    nodes={name:Node(name) for name in g}#nodes字典记录了暂时的最优解
    start=nodes[r]
    start.dist=0
    q=[]
    heapq.heappush(q,start)
    quanzhi=0
    visited=set()
    while q:
        now=heapq.heappop(q)
        if now.name in visited:#已经被操作过了，等效于visited=True
            continue
        if now.prev:
            quanzhi+=now.dist
        visited.add(now.name)
        for edge in g[now.name]:
            nei=nodes[edge.c]
            newdist=edge.value
            if newdist<nei.dist:
                nei.dist=newdist
                nei.prev=now
                heapq.heappush(q,Node(edge.c,now,newdist))
    return quanzhi
g = {}
# 初始化所有节点的邻接表
for c in range(n):
    node_name = chr(ord('A') + c)
    g[node_name] = []

# 读取n-1行数据
for _ in range(n-1):
    parts = input().split()
    current_node = parts[0]
    k = int(parts[1])
    edges_info = parts[2:]
    for i in range(k):
        neighbor = edges_info[i*2]
        value = int(edges_info[i*2 + 1])
        g[current_node].append(Edge(neighbor, value))
        # 添加反向边（无向图）
        g[neighbor].append(Edge(current_node, value))

print(prim(g, 'A'))





