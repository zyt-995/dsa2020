class UnionFind:
    """并查集（Union-Find）数据结构，用于检测环"""
    def __init__(self, nodes):
        self.parent = {node: node for node in nodes}  # 父节点字典

    def find(self, u):
        """查找节点u的根节点（带路径压缩）"""
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        ru=self.find(u)
        rv=self.find(v)
        if ru == rv:
            return True
        else:
            self.parent[rv] = ru
            return False
while True:
    try:
        n,m = map(int, input().split())
        nodes=set(i for i in range(1,n+1))
        uf = UnionFind(nodes)
        for i in range(m):
            u,v=map(int,input().split())
            if uf.union(u,v):
                print("Yes")
            else:
                print("No")
        ans=[]
        for i in nodes:
            if uf.find(i) ==i:
                ans.append(i)
        print(len(ans))
        print(*ans)
    except EOFError:
        break


