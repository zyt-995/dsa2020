'''
描述
在一个给定形状的棋盘（形状可能是不规则的）上面摆放棋子，棋子没有区别。要求摆放时任意的两个棋子不能放在棋盘中的同一行或者同一列，请编程求解对于给定形状和大小的棋盘，摆放k个棋子的所有可行的摆放方案C。
输入
输入含有多组测试数据。
每组数据的第一行是两个正整数，n k，用一个空格隔开，表示了将在一个n*n的矩阵内描述棋盘，以及摆放棋子的数目。 n <= 8 , k <= n
当为-1 -1时表示输入结束。
随后的n行描述了棋盘的形状：每行有n个字符，其中 # 表示棋盘区域， . 表示空白区域（数据保证不出现多余的空白行或者空白列）。
输出
对于每一组数据，给出一行输出，输出摆放的方案数目C （数据保证C<2^31）。
样例输入
2 1
#.
.#
4 4
...#
..#.
.#..
#...
-1 -1
样例输出
2
1
'''
plan=0
def place(gra,available_colomn,remain_chess,cur_row,n):
    global plan
    if cur_row>n and remain_chess:
        return
    if remain_chess==0:
        plan+=1
        return
    if cur_row+remain_chess>n+1:
        return
    place(gra,available_colomn,remain_chess,cur_row+1,n)
    for i in range(1,n+1):
        if gra[cur_row][i]=='#' and available_colomn[i]==0:
            available_colomn[i]=1
            place(gra,available_colomn,remain_chess-1,cur_row+1,n)
            available_colomn[i]=0
    return


while True:
    n,k=map(int,input().split())
    if n==-1:
        break
    gra=[['.']*(n+2) for _ in range(n+2)]
    for i in range(1,n+1):
        d=list(input())
        for j in range(1,n+1):
            gra[i][j]=d[j-1]
    plan=0
    available_colomn=[0]*10
    place(gra,available_colomn,k,1,n)
    print(plan)

