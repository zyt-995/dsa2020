class UnionFind:
    def __init__(self,size):
        self.parent = list(range(size+1))
    def find(self,x):
        if self.parent[x]!=x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    def union(self,x,y):
        xroot=self.find(x)
        yroot=self.find(y)
        if xroot==yroot:
            return
        self.parent[yroot]=xroot
n,m=map(int,input().split())
uf=UnionFind(n)
for i in range(m):
    x,y=map(int,input().split())
    uf.union(x,y)
roots=set()
for i in range(1,n+1):
    roots.add(uf.find(i))
print(len(roots))



