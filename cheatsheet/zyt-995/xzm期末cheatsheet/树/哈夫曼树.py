import heapq
class Node:#其实也就是初始化树的过程，Node改名叫Tree也没问题
    def __init__(self,fre,charr,left=None,right=None):
        self.fre,self.charr,self.left,self.right=fre,charr,left,right
    def __lt__(self,other):#定义一个特殊的比较方法，如果自身更小就返回True
        if self.fre!=other.fre:
            return self.fre<other.fre
        return self.charr<other.charr
n=int(input())
nodes=[]
for _ in range(n):
    charr,fre=input().split()
    fre=int(fre)
    node=Node(fre,charr)#要按照Node数据类型输入，这样的话给后面的排序会有简化
    nodes.append(node)
heapq.heapify(nodes)#按照Node数据类型的规则，把nodes这个list进行从小到大建堆
while len(nodes)>1:#这时标准的通过堆来建立哈夫曼树的过程，有推广意义。注意这一行，当长度为1的时候就已经建立完成
    left=heapq.heappop(nodes)
    right=heapq.heappop(nodes)
    jia_fre=left.fre+right.fre
    jia_charr=min(left.charr,right.charr)#注意这里要取最小的字符，才能保证合并的节点和其他节点比较的时候不会出bug
    jia=Node(jia_fre,jia_charr,left,right)
    heapq.heappush(nodes,jia)
tree=nodes[0]#成功建立一棵哈夫曼树！
#以上都是具有一般性的操作，可以重点学习

#下面利用哈夫曼树创立编码表
bmb={}
def bianma(tree,path):#利用递推的办法创立,这个和递归有一点点不一样，学习一下
    if tree.left==None and tree.right==None:#说明这个是叶节点，也就是递推终止
        bmb[tree.charr]=path
        return#避免无限递推
    bianma(tree.left,path+'0')
    bianma(tree.right,path+'1')
bianma(tree,'')
while True:
    try:
        s=input()
        first=s[0]
        if first.isalpha():#isalpha函数判断是否为字母，是的话返回True
            #是字母，进行编码
            result=''
            for i in range(len(s)):
                result=result+bmb[s[i]]
            print(result)
        else:
            result1=''
            know=tree
            for j in range(len(s)):
                if s[j]=='1':
                    know=know.right
                if s[j]=='0':
                    know=know.left
                if know.left==None and know.right==None:
                    result1=result1+know.charr
                    know=tree
            print(result1)
    except:
        break