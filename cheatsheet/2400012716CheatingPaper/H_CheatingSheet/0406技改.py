'''
描述
给一个由1跟0组成的方形地图，1代表土地，0代表水域

相邻(上下左右4个方位当作相邻)的1组成孤岛

现在你可以将0转成1，搭建出一个链接2个孤岛的桥

请问最少要将几个0转成1，才能建成链接孤岛的桥。

题目中恰好有2个孤岛(顾答案不会是0)



输入
一个正整数n，代表几行输入
n行0跟1字串
输出
一个正整数k，代表最短距离
样例输入
3
110
000
001
样例输出
2
提示
样例输入中的两个孤岛最短距离为2
'''


def mark(x,y):
    if x not in range(n) or y not in range(n):
        return
    if map[x][y]=='1':
        map[x][y]=2
        mark(x-1,y)
        mark(x,y-1)
        mark(x,y+1)
        mark(x+1,y)
    return
        
def search(x,y):
    if (x==0 or map[x-1][y]==2)and(x==n-1 or map[x+1][y]==2)and(y==0 or map[x][y-1]==2)and(y==n-1 or map[x][y+1]==2):
        return 2*n
    else:
        min_distance=2*n
        for i in range(n):
            for j in range(n):
                if map[i][j]=='1':
                    min_distance=min(min_distance,abs(x-i)+abs(y-j)-1)
        return min_distance
    

n=int(input())
map=[]
for i in range(n):
    map.append(list(input()))
Is_marked=False
for i in range(n):
    for j in range(n):
        if map[i][j]=='1':
            mark(i,j)
            Is_marked=True
            break
    if Is_marked:
        break
shortest_bridge=n*2
for i in range(n):
    for j in range(n):
        if map[i][j]==2:
            shortest_bridge=min(shortest_bridge,search(i,j))
print(shortest_bridge)
