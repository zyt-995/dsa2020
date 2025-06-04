'''
输入
第一行只包含一个表示星星个数的数n，n不大于26，并且这n个星星是由大写字母表里的前n个字母表示。接下来的n-1行是由字母表的前n-1个字母开头。最后一个星星表示的字母不用输入。对于每一行，以每个星星表示的字母开头，然后后面跟着一个数字，表示有多少条边可以从这个星星到后面字母表中的星星。如果k是大于0，表示该行后面会表示k条边的k个数据。每条边的数据是由表示连接到另一端星星的字母和该边的权值组成。权值是正整数的并且小于100。该行的所有数据字段分隔单一空白。该星星网络将始终连接所有的星星。该星星网络将永远不会超过75条边。没有任何一个星星会有超过15条的边连接到其他星星（之前或之后的字母）。在下面的示例输入，数据是与上面的图相一致的。
输出
输出是一个整数，表示最小的权值和
样例输入
9
A 2 B 12 I 25
B 3 C 10 H 40 I 8
C 2 D 18 G 55
D 1 E 44
E 2 F 60 G 38
F 0
G 1 H 35
H 1 I 35
样例输出
216
'''

class Graph():
    def __init__(self):
        self.vertlist={}

class Vertex():
    def __init__(self,key):
        self.nbrs={}
        self.id=key 
        self.indgree=self.outdegree=0
    
    def addNei(self,nbr,weight=1):
        if nbr not in self.nbrs:
            self.nbrs[nbr]=weight

n=int(input())
stLink=Graph()
dis=0
for i in range(n):
    new_vert=chr(ord('A')+i)
    stLink.vertlist[new_vert]=Vertex(new_vert)
for i in range(n-1):
    links=list(input().split())
    start=stLink.vertlist[links[0]]
    for i in range(int(links[1])):
        start.addNei(links[2*i+2],int(links[2*i+3]))
        stLink.vertlist[links[2*i+2]].addNei(start.id,int(links[2*i+3]))

cur_ver=stLink.vertlist['A']
getConnected=['A']
available_edge=[]
for _ in range(n-1):
    for item in cur_ver.nbrs.keys():
        if item not in getConnected:
            available_edge.append([cur_ver.id,item,cur_ver.nbrs[item]])
    available_edge.sort(key=lambda x:x[2],reverse=True)
    getEdge=available_edge.pop()
    dis+=getEdge[2]
    for item in available_edge:
        if item[1]==getEdge[1]:
            available_edge.remove(item)
    cur_ver=stLink.vertlist[getEdge[1]]
    getConnected.append(cur_ver.id)
print(dis)
        
        

    


    

