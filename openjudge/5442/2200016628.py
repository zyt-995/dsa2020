import sys

# 读取顶点数
n = int(input())
# 初始化邻接矩阵，这里用二维列表模拟，初始值设为无穷大
graph = [[sys.maxsize] * n for _ in range(n)]
for i in range(n - 1):
    line = input().split()
    vertex = ord(line[0]) - ord('A')
    num_edges = int(line[1])
    for j in range(num_edges):
        neighbor = ord(line[2 * j + 2]) - ord('A')
        weight = int(line[2 * j + 3])
        graph[vertex][neighbor] = weight
        graph[neighbor][vertex] = weight  # 无向图，双向赋值

# 标记顶点是否已加入最小生成树
in_mst = [False] * n
# 存储每个顶点到最小生成树的最小边权，初始设为无穷大
key = [sys.maxsize] * n
# 从第一个顶点开始，将其key设为0
key[0] = 0
mst_weight = 0

for _ in range(n):
    min_key = sys.maxsize
    min_index = 0
    # 找到未加入最小生成树且边权最小的顶点
    for v in range(n):
        if not in_mst[v] and key[v] < min_key:
            min_key = key[v]
            min_index = v
    # 将该顶点加入最小生成树
    in_mst[min_index] = True
    mst_weight += min_key
    # 更新与该顶点相邻的顶点的key值
    for v in range(n):
        if (
            graph[min_index][v] != sys.maxsize
            and not in_mst[v]
            and graph[min_index][v] < key[v]
        ):
            key[v] = graph[min_index][v]

print(mst_weight)