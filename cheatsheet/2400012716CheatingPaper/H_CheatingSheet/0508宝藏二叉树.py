'''
描述
探险家小B发现了一颗宝藏二叉树。这棵树的树根为Root，除了Root节点之外，每个节点均只有一个父节点，因此形成了一颗二叉树。宝藏二叉树的每个节点都有宝藏，每个宝藏具有相应的价值。小B希望摘取这些宝藏，使自己的收益最大。可是，宝藏二叉树有一个奇怪的性质，在摘取宝藏的时候，如果两个节点之间有边，那么最多只能摘取其中一个节点上的宝藏，如果因为贪婪而把两个节点上的宝藏都摘取，二叉树就会立即消失，丧失所有奖励。为此，小B求助于你，希望你能给出，小B在不使宝藏二叉树消失的前提下，能够获得宝藏的最大价值。

为了简化题目，规定宝藏二叉树均为完全二叉树，树中节点如图所示自上而下，自左向右，从1-N编号。

输入
输入分为两行
第一行为一个整数N，代表二叉树中节点的个数。
第二行为一个N个非负整数。第i个数代表二叉树中编号为i的节点上的宝藏价值。
输出
输出为一个整数，代表小B的最大收益。
'''

def max_treasure(r):
    if r>N:
        return 0
    if r*2>N:
        return treasure[r]
    else:
        a=max_treasure(2*r)+max_treasure(2*r+1)
        b=treasure[r]+max_treasure(4*r)+max_treasure(4*r+1)+max_treasure(4*r+2)+max_treasure(4*r+3)
        return max(a,b)


N=int(input())
treasure=[0]*(2*N+5)
treasure[1:N+1]=map(int,input().split())
print(max_treasure(1))
