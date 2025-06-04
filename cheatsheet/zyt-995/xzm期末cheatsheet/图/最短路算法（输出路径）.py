import heapq
class Edge:
    def __init__(self,c,value):
        self.c=c
        self.value=value
    def __lt__(self,other):
        return self.value<other.value
class Node:
    def __init__(self,name,prev=None,dist=float('inf')):
        self.name=name
        self.prev=prev
        self.dist=dist
    def __lt__(self,other):
        return self.dist<other.dist
def dij(g,r,c):
    n=len(g)
    q=[]
    nodes={name:Node(name) for name in g}#存储最终结果,会随着后续操作儿变化！！！
    start=nodes[r]
    start.dist=0
    heapq.heappush(q,start)
    while len(q)>0:
        now=heapq.heappop(q)
        if now.name==c:
            break
        if now.dist>nodes[now.name].dist:
            continue#直接跳过循环，避免重复处理已经出队的node
        for edge in g[now.name]:#不要新建一个node，否则会导致prev断裂！！！
            neighbor_node = nodes[edge.c]  # 获取已存在的节点对象
            new_dist = now.dist + edge.value
            if new_dist < neighbor_node.dist:  # 比较距离
                neighbor_node.dist = new_dist  # 直接更新属性
                neighbor_node.prev = now  # 直接更新属性
                heapq.heappush(q, Node(edge.c, now, new_dist))  # 仅用于队列排序的临时节点
    path=[]
    current=nodes[c]
    while current:
        path.append(current.name)
        current=current.prev
    path.reverse()
    if path==[]:
        return None
    else:
        return path
n=int(input())
g={}
for _ in range(n):
    name=input()
    g[name]=[]
m=int(input())
for _ in range(m):
    begin,c,value=input().split()
    g[begin].append(Edge(c,int(value)))
    g[c].append(Edge(begin,int(value)))
r=int(input())
for _ in range(r):
    r,c=input().split()
    answer=dij(g,r,c)
    if len(answer)==1:
        print(answer[0])
    else:
        output=[]
        for i in range(len(answer)-1):
            start=answer[i]
            end=answer[i+1]
            for edge in g[start]:
                if edge.c==end:
                    output.append(f'{start}->({edge.value})')
                    break
        output.append(c)
        print('->'.join(output))