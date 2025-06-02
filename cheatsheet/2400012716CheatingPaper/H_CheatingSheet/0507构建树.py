'''
7:简单的树上最近公共祖先查询
查看提交统计提问
总时间限制: 10000ms 单个测试点时间限制: 1000ms 内存限制: 262144kB
描述
给出一棵包含 N 个节点的有根树，节点编号 1 到 N，根节点为 R。请回答 Q 个查询，计算节点 u 和节点 v 的最近公共祖先。

祖先定义：任意节点 u 到根节点 R 的路径上的所有点（包括 u 和 R 在内）称为节点 u 的祖先。

最近公共祖先定义：节点 u 和节点 v 的公共祖先中，深度最深的那个节点被称为节点 u 和 v 的最近公共祖先（也可以直观理解为距离它们最近的公共祖先）。

例如，下图是以 1 号节点为根的有根树，其中 11 和 13 的最近公共祖先为 5，2 和 8 的最近公共祖先为 1，19 和 21 的最近公共祖先为 9，16 和 1 的最近公共祖先为 1，15 和 15 的最近公共祖先为 15。



输入
第一行包含两个整数 N, R (1<=R<=N<=1000) 分别表示节点总数和根结点编号。
接下来 N-1 行，每行表示一条边，包含两个整数 u, v (1<=u,v<=N, u≠v)。输入保证全部节点构成一棵树。
接下来一行，包含一个整数 Q (1<=Q<=2000) 表示询问次数。
接下来 Q 行，每行两个整数 x, y (1<=x,y<=N) 表示询问节点 x 和 节点 y 的最近公共祖先。
输出
一共 Q 行，每行一个整数表示答案。
样例输入
21 1
1 2
1 3
1 4
2 5
3 6
3 7
8 4
9 4
10 4
11 5
12 5
13 5
14 7
9 15
16 9
17 9
9 18
16 19
16 20
18 21
10
19 20
19 18
16 10
12 21
11 6
2 5
3 9
14 6
17 1
15 15
样例输出
16
9
4
1
1
2
1
3
1
15
'''

cur_tree=1

class tree_node():
    def __init__(self,data,father=None):
        self.data=data
        self.child=[]
        self.father=father
        
def BuildTree(r,cur_tree):
    posible_child=tree_link.get(r)
    for item in posible_child:
        if is_exist[item]==0:
            cur_tree.child.append(tree_node(item,cur_tree.data))
            is_exist[item]=1
            stack.append(cur_tree)
            cur_tree=cur_tree.child[-1]
            BuildTree(item,cur_tree)
            cur_tree=stack.pop()
        else:
            father[r]=item

def get_father(t):
    if t!=father[t]:
        return get_father(father[t])+[t]         
    else:
        return [t]

N,R=map(int,input().split())
tree_link={}
for _ in range(N-1):
    a,b=map(int,input().split())
    tree_link[a]=[b]+tree_link.get(a,[])
    tree_link[b]=[a]+tree_link.get(b,[])
tree=cur_tree=tree_node(R)
is_exist=[0]*1005
is_exist[R]=1
stack=[]
father=[[] for _ in range(1005)]
father[R]=R
BuildTree(R,cur_tree)
Q=int(input())
for _ in range(Q):
    x,y=map(int,input().split())
    x=get_father(x)
    while y!=R:
        if y in x:
            break
        else:
            y=father[y]
    print(y)





