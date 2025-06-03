from collections import deque
#topo排序
def topo(graph):
    degree={u:0 for u in graph}
    for u in graph:
        for v in graph[u]:
            degree[v]+=1
    queue=deque([u for u in graph if degree[u]==0])
    result=[]
    unique=True
    while queue:
        if len(queue)>1:
            unique=False
        u=queue.popleft()
        result.append(u)
        for v in graph[u]:
            degree[v]-=1
            if degree[v]==0:
                queue.append(v)
    if len(result)!=n:
        return "Inconsistency",None
    if unique:
        return "determined","".join(result)
    return "not determined", None
while True:
    n,m=map(int,input().split())
    if n==0 and m==0:
        break
    graph={chr(i+ord("A")):[] for i in range(n)}
    for _ in range(m):
        a,b=map(str,input().split("<"))
        graph[a].append(b)
        statu,seq=topo(graph)
        if statu=="Inconsistency":
            print(f"Inconsistency found after {_+1} relations.")
            for l in range(_+1,m):
                input()
            break
        elif statu=="determined":
            print(f"Sorted sequence determined after {_+1} relations: {seq}.")
            for l in range(_+1,m):
                input()
            break
        elif _==m-1 and statu=="not determined":
            print("Sorted sequence cannot be determined.")
            for l in range(_+1,m):
                input()
            break




