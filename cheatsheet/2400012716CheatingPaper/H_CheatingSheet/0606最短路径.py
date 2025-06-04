'''
描述
You have just moved from a quiet Waterloo neighbourhood to a big, noisy city. Instead of getting to ride your bike to school every day, you now get to walk and take the subway. Because you don't want to be late for class, you want to know how long it will take you to get to school.
You walk at a speed of 10 km/h. The subway travels at 40 km/h. Assume that you are lucky, and whenever you arrive at a subway station, a train is there that you can board immediately. You may get on and off the subway any number of times, and you may switch between different subway lines if you wish. All subway lines go in both directions.
输入
Input consists of the x,y coordinates of your home and your school, followed by specifications of several subway lines. Each subway line consists of the non-negative integer x,y coordinates of each stop on the line, in order. You may assume the subway runs in a straight line between adjacent stops, and the coordinates represent an integral number of metres. Each line has at least two stops. The end of each subway line is followed by the dummy coordinate pair -1,-1. In total there are at most 200 subway stops in the city.
输出
Output is the number of minutes it will take you to get to school, rounded to the nearest minute, taking the fastest route.
样例输入
0 0 10000 1000
0 200 5000 200 7000 200 -1 -1 
2000 600 5000 600 10000 600 -1 -1
样例输出
21
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
  

subways=Graph()
pos=list(map(int,input().split()))
home=tuple(pos[0:2])
school=tuple(pos[2:])
subways.vertlist[home]=Vertex(home)
subways.vertlist[school]=Vertex(school)
home_school=((home[1]-school[1])**2+(home[0]-school[0])**2)**0.5
walk=10000/60
ride=40000/60
subways.vertlist[home].addNei(subways.vertlist[school].id,(home_school/walk))
subways.vertlist[school].addNei(subways.vertlist[home].id,(home_school/walk))
while True:
    try:
        s=input()
        subway=list(map(int,s.split()))
        stations=[]
        for i in range(len(subway)//2-1):
            station=tuple(subway[2*i:2*i+2])
            if station not in subways.vertlist:
                cur_pos=subways.vertlist[station]=Vertex(station) 
            else:
                cur_pos=subways.vertlist[station]
            for item in subways.vertlist.values():
                distance=((cur_pos.id[1]-item.id[1])**2+(cur_pos.id[0]-item.id[0])**2)**0.5
                cur_pos.addNei(item.id,distance/walk)
                item.addNei(cur_pos.id,distance/walk)
            for item in stations:
                distance=((cur_pos.id[1]-item.id[1])**2+(cur_pos.id[0]-item.id[0])**2)**0.5
                cur_pos.addNei(item.id,distance/ride)
                item.addNei(cur_pos.id,distance/ride)
            if len(stations):
                stations.pop()
            stations.append(cur_pos)
    except EOFError:
        break



dijkstra(subways,subways.vertlist[home])
if subways.vertlist[school].dis-int(subways.vertlist[school].dis)<0.5:
    print(int(subways.vertlist[school].dis))
else:
    print(int(subways.vertlist[school].dis)+1)


