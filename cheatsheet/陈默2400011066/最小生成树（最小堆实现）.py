import heapq


def prim_mst_heap(graph):
    """基于最小堆的Prim算法实现
    :param graph: 邻接表形式的带权图，graph[u]包含(v, weight)元组列表
    :return: (mst总权重, 边集合)
    """
    n = len(graph)
    key = [float('inf')] * n  # 节点到MST的最小权重
    parent = [-1] * n  # 父节点记录
    visited = [False] * n  # 访问标记
    heap = []

    # 初始化：从节点0开始（可任选起始点）
    start_node = 0
    key[start_node] = 0
    heapq.heappush(heap, (0, start_node, -1))  # (权重, 当前节点, 父节点)

    mst_edges = []
    total_weight = 0

    while heap:
        weight, u, pu = heapq.heappop(heap)

        if visited[u]:
            continue

        visited[u] = True
        total_weight += weight
        if pu != -1:# 起始节点无父节点
            if pu>u:
               mst_edges.append((weight,(u, pu)))
            else:
                mst_edges.append((weight,(pu, u)))
        # 遍历邻接节点
        for v, w in graph[u]:
            if not visited[v] and w < key[v]:
                key[v] = w
                parent[v] = u
                heapq.heappush(heap, (w, v, u))
    mst_edges.sort()
    return (total_weight, mst_edges) if len(mst_edges) == n - 1 else (None,[])
n,m=map(int,input().split())
graph=[[] for i in range(n)]
for i in range(m):
    s,e,w=map(float,input().split())
    graph[int(s)].append((int(e),w))
    graph[int(e)].append((int(s),w))
sta,edges=prim_mst_heap(graph)
if sta:
    print(f"{sta:.2f}")
    for i,j in edges:
        print(*j)
else:
    print("NOT CONNECTED")



