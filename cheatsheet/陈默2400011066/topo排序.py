from collections import deque


def topological_sort(num_nodes, edges):
    # 初始化入度表和邻接表
    in_degree = [0] * num_nodes
    adjacency = [[] for _ in range(num_nodes)]

    # 构建图结构
    for u, v in edges:
        adjacency[u].append(v)  # u -> v的有向边
        in_degree[v] += 1

    # 将初始入度为0的节点加入队列
    queue = deque([i for i in range(num_nodes) if in_degree[i] == 0])
    result = []

    # Kahn算法核心过程
    while queue:
        node = queue.popleft()
        result.append(node)

        # 处理当前节点的所有邻接节点
        for neighbor in adjacency[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # 检查是否存在环
    if len(result) != num_nodes:
        return []  # 存在环，返回空列表
    return result


# 示例测试
if __name__ == "__main__":
    # 测试用例：课程依赖关系 (4个节点)
    # 边表示 u -> v 的依赖关系，即v依赖于u
    edges = [(1, 0), (2, 0), (1, 3)]
    print(topological_sort(4, edges))  # 可能的输出：[1, 2, 0, 3] 或 [2, 1, 0, 3]

    # 测试有环情况
    cyclic_edges = [(0, 1), (1, 2), (2, 0)]
    print(topological_sort(3, cyclic_edges))  # 输出空列表，表示有环