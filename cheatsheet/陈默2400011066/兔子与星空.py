class UnionFind:
    """并查集（Union-Find）数据结构，用于检测环"""
    def __init__(self, nodes):
        self.parent = {node: node for node in nodes}  # 父节点字典
        self.rank = {node: 0 for node in nodes}      # 秩（用于路径优化）

    def find(self, u):
        """查找节点u的根节点（带路径压缩）"""
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        """合并两个节点的集合（按秩合并）"""
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u != root_v:
            # 按秩合并，小秩合并到大秩
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            else:
                self.parent[root_u] = root_v
                if self.rank[root_u] == self.rank[root_v]:
                    self.rank[root_v] += 1

def kruskal(edges, nodes):
    """Kruskal算法实现"""
    edges_sorted = sorted(edges, key=lambda x: x[2])  # 按边权升序排序
    uf = UnionFind(nodes)
    mst = 0
    count=0
    for edge in edges_sorted:
        u, v, weight = edge
        if uf.find(u) != uf.find(v):
            uf.union(u, v)
            mst+=weight
            count+=1
        if count == len(nodes) - 1:  # 生成树边数达到n-1时终止
            break
    return mst
n=int(input())
edges=[]
for i in range(n-1):
    s=list(map(str,input().split()))
    if len(s)>2:
        for j in range(2,len(s)):
            if s[j].isalpha():
                edges.append((s[0],s[j],int(s[j+1])))
nodes={chr(ord('A')+i) for i in range(n)}
print(kruskal(edges, nodes))


