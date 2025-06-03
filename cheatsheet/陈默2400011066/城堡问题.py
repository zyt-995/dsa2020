from collections import deque
def topo(graph):
    degree={u:0 for u in graph}
    for u in graph:
        for v in graph[u]:
            degree[v]+=1
    queue=deque([u for u in degree if degree[u]==0])
    result=[]
    unique=True#如果队列中有多个顶点，也说明排序不唯一
    while queue:
        if len(queue)>1:
            unique=False
        u=queue.popleft()
        result.append(u)
        for v in graph[u]:
            degree[v]-=1
            if degree[v]==0:
                queue.append(v)
    if len(result) != n:
        return "conflict", None
            # 检测是否唯一排序
    if unique:
        return "determined", "".join(result)
    else:
        return "undetermined", None
while True:
    n,m=map(int,input().split())
    if n==m==0:
        break
    graph = {chr(ord('A') + i): [] for i in range(n)}

    answer = ""
    for i in range(m):
        a,b=map(str,input().split("<"))
        graph[a].append(b)
        status,seq=topo(graph)
        if status=="conflict":
            print(f"Inconsistency found after {i+1} relations.")
            for _ in range(i+1,m):
                input()
            break
        elif status=="determined":
            print(f"Sorted sequence determined after {i+1} relations: {seq}.")
            for _ in range(i+1,m):
                input()
            break
        elif i==m-1 :
            print(f"Sorted sequence cannot be determined.")
            for _ in range(i+1,m):
                input()
            break