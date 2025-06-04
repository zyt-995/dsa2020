import heapq
graph={}
p=int(input())
for i in range(p):
    place=input()
    graph[place]={}
q=int(input())
for i in range(q):
    a,b,d=map(str,input().split())
    d=int(d)
    graph[a][b]=d
    graph[b][a]=d
def dijkstra(start,end):
    heaq=[(0,start)]
    dists={u:float("inf") for u in graph}
    dists[start]=0
    parent={node:None for node in graph}
    while heaq:
        dist,curr=heapq.heappop(heaq)
        if curr==end:
            break
        if dists[curr]<dist:
            continue
        for k,v in graph[curr].items():
            if dist+v<dists[k]:
                dists[k]=dist+v
                heapq.heappush(heaq,(dists[k],k))
                parent[k]=curr
    if not parent[end] and end!=start:
        return
    path=[]
    node=end
    while node:
        path.append(node)
        temp=parent[node]
        if temp:
            path.append(f"({graph[temp][node]})")
        node=temp
    return "->".join(path[::-1])
r=int(input())
for i in range(r):
    s1,s2=map(str,input().split())
    print(dijkstra(s1,s2))
