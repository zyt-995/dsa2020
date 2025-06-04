'''
描述
     1   2   3   4   5   6   7  
   #############################
 1 #   |   #   |   #   |   |   #
   #####---#####---#---#####---#
 2 #   #   |   #   #   #   #   #
   #---#####---#####---#####---#
 3 #   |   |   #   #   #   #   #
   #---#########---#####---#---#
 4 #   #   |   |   |   |   #   #
   #############################
           (图 1)

   #  = Wall   
   |  = No wall
   -  = No wall

图1是一个城堡的地形图。请你编写一个程序，计算城堡一共有多少房间，最大的房间有多大。城堡被分割成m×n(m≤50，n≤50)个方块，每个方块可以有0~4面墙。

输入
程序从标准输入设备读入数据。第1、2行每行1个整数，分别是南北向、东西向的方块数。在接下来的输入行里，每个方块用一个数字(0≤p≤50)描述。用一个数字表示方块周围的墙，1表示西墙，2表示北墙，4表示东墙，8表示南墙。每个方块用代表其周围墙的数字之和表示。城堡的内墙被计算两次，方块(1,1)的南墙同时也是方块(2,1)的北墙。输入的数据保证城堡至少有两个房间。
输出
输出2行，每行一个数，表示城堡的房间数、城堡中最大房间所包括的方块数。结果显示在标准输出设备上。
样例输入
4 
7 
11 6 11 6 3 10 6 
7 9 6 13 5 15 5 
1 10 12 7 13 7 5 
13 11 10 8 10 12 13 
样例输出
5
9
'''

def count(x,y):
    if castle[x][y]==-1:
        return 0
    vis[x][y]=1
    size=1
    if castle[x+1][y]&2==0 and vis[x+1][y]==0:
        size+=count(x+1,y)
    if castle[x-1][y]&8==0 and vis[x-1][y]==0:
        size+=count(x-1,y)
    if castle[x][y+1]&1==0 and vis[x][y+1]==0:
        size+=count(x,y+1)
    if castle[x][y-1]&4==0 and vis[x][y-1]==0:
        size+=count(x,y-1)
    return size



r=int(input())
c=int(input())
castle=[[-1]*(c+3) for _ in range(r+3)]
vis=[[0]*(c+3) for _ in range(r+3)]
for i in range(1,r+1):
    T=list(map(int,input().split()))
    for j in range(1,c+1):
        castle[i][j]=T[j-1]
room=0
max_size=0
for i in range(1,r+1):
    for j in range(1,c+1):
        if vis[i][j]==0:
            room+=1
            size=count(i,j)
            if size>max_size:
                max_size=size
print(room)
print(max_size)


