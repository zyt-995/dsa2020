'''
描述
很久很久之前，森林里住着一群兔子。有一天，兔子们希望去赏樱花，但当他们到了上野公园门口却忘记了带地图。现在兔子们想求助于你来帮他们找到公园里的最短路。

输入
输入分为三个部分。
第一个部分有P+1行（P<30），第一行为一个整数P，之后的P行表示上野公园的地点, 字符串长度不超过20。
第二个部分有Q+1行（Q<50），第一行为一个整数Q，之后的Q行每行分别为两个字符串与一个整数，表示这两点有直线的道路，并显示二者之间的矩离（单位为米）。
第三个部分有R+1行（R<20），第一行为一个整数R，之后的R行每行为两个字符串，表示需要求的路线。
输出
输出有R行，分别表示每个路线最短的走法。其中两个点之间，用->(矩离)->相隔。
样例输入
6
Ginza
Sensouji
Shinjukugyoen
Uenokouen
Yoyogikouen
Meijishinguu
6
Ginza Sensouji 80
Shinjukugyoen Sensouji 40
Ginza Uenokouen 35
Uenokouen Shinjukugyoen 85
Sensouji Meijishinguu 60
Meijishinguu Yoyogikouen 35
2
Uenokouen Yoyogikouen
Meijishinguu Meijishinguu
样例输出
Uenokouen->(35)->Ginza->(80)->Sensouji->(60)->Meijishinguu->(35)->Yoyogikouen
Meijishinguu
'''


class Graph():
    def __init__(self):
        self.vertlist={}

class Vertex():
    def __init__(self,key):
        self.nbrs={}
        self.id=key 
        self.indgree=self.outdegree=0
        self.pre=None
        self.dis=0
    
    def addNei(self,nbr,weight=1):
        self.nbrs[nbr]=weight

   
import sys
def dijkstra(g, start):#gragh,vertex类
    for item in g.vertlist.values():
        item.dis=sys.maxsize
        item.pre=None
    quequ=[start]
    start.dis=0
    while len(quequ):
        cur_vertex=quequ.pop(0)
        for item in cur_vertex.nbrs:
            newDis=cur_vertex.dis+cur_vertex.nbrs[item]
            if newDis<g.vertlist[item].dis:
                g.vertlist[item].dis=newDis
                g.vertlist[item].pre=cur_vertex
                quequ.append(g.vertlist[item])
  

park=Graph()
P=int(input())
for _ in range(P):
    site=input()
    park.vertlist[site]=Vertex(site)
Q=int(input())
for _ in range(Q):
    path=list(input().split())
    fr,to,dis=path
    dis=int(dis)
    park.vertlist[fr].addNei(to,dis)
    park.vertlist[to].addNei(fr,dis)
R=int(input())
for _ in range(R):
    start,end=input().split()
    if start==end:
        print(start)
    else:
        dijkstra(park,park.vertlist[start])
        way=[]
        position=park.vertlist[end]
        while True:
            way.append(position.id)
            if position.pre:
                way.append(position.dis-position.pre.dis)
                position=position.pre
            else:
                break
        while len(way):
            item=way.pop()
            if item!=end:
                if type(item)==str:
                    print(item,end="->(")
                else:
                    print(item,end=")->")
            else:
                print(end)
                    
            



    


