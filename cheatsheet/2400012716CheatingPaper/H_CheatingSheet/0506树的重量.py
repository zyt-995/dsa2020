
'''
描述
有一棵 k 层的满二叉树（一共有2k-1个节点，且从上到下从左到右依次编号为1, 2, ..., 2k-1），最开始每个节点的重量均为0。请编程实现如下两种操作：

1 x y：给以 x 为根的子树的每个节点的重量分别增加 y（ y 是整数且绝对值不超过100）
2 x：查询（此时的）以 x 为根的子树的所有节点重量之和

输入
输入有n+1行。第一行是两个整数k, n，分别表示满二叉树的层数和操作的个数。接下来n行，每行形如1 x y或2 x，表示一个操作。

k<=15（即最多32767个节点），n<=50000。
输出
输出有若干行，对每个查询操作依次输出结果，每个结果占一行。
样例输入
3 7
1 2 1
2 4
1 6 3
2 1
1 3 -2
1 4 1
2 3
样例输出
1
6
-3
提示
可以通过对数计算某节点的深度：

import math

math.log2(x)  #以小数形式返回x的对数值，注意x不能为0
'''

import math

k,n=map(int,input().split())
tree=[[0,0] for _ in range(32770)]#w[i],weight[i]
treesize=lambda i:2**(k-int(math.log2(i)))-1
for _ in range(n):
    oper=list(map(int,input().split()))
    if oper[0]==1:
        p=oper[1]
        delta=oper[2]
        tree[p][0]+=delta
        while p>0:           
            tree[p][1]+=delta*treesize(oper[1])
            p=p//2
    else:
        q=oper[1]
        sum=tree[q][1]
        while q>1:
            q=q//2
            sum+=tree[q][0]*treesize(oper[1])
        print(sum)

