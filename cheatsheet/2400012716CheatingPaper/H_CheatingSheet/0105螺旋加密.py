'''
描述
Chip和Dale发明了一种文本信息加密技术。他们事先秘密约定好矩阵的行数和列数。接着，将字符按如下方式编码：

1. 所有文本只包含大写字母和空格。

2. 每个字符均赋予一个数值：空格=0，A=1，B=2，……，Y=25，Z=26。

按照下图所示的方式，将每个字符对应数值的5位二进制数依次填入矩阵。最后用0将矩阵补充完整。例如，对于信息“ACM”，行列数均为4时，矩阵将被填充为：



将矩阵中的数字按行连起来形成数字串，完成加密。例子中的信息最终会被加密为：0000110100101100。

输入
一行。首先是两个整数R(1≤R≤20)和C(1≤C≤20)，表示行数和列数。之后是一个只包含大写字母和空格的字符串。字符串的长度≤(R*C)/5。R和C之间以及C和字符串之间均用单个空格隔开。
输出
一行，为加密后的二进制串。注意你可能需要用0将矩阵补充完整。
样例输入
4 4 ACM
样例输出
0000110100101100
'''


user_input=input()
items=user_input.split(" ",2)
R=int(items[0])
C=int(items[1])
string=items[2]
encode=[[2 for _ in range(C)] for _ in range(R)]#二维数组，存储答案
trans=[]#储存二进制数列
for i in range(len(string)):#把每一单词变成五位数的二进制
    if string[i]==" ":
        trans+=[0]*5
    else:
        letter_id=ord(string[i])-ord('A')+1
        for _ in range(5):
            trans.insert(i*5,letter_id%2)
            letter_id=letter_id//2
while(len(trans)<R*C):
    trans+=[0]
x,y=0,0
dirs=([0,1],[1,0],[0,-1],[-1,0])#右下左上
dir=0
for i in range(R*C):
    encode[x][y]=trans[i]
    if x+dirs[dir][0]<R and y+dirs[dir][1]<C and x+dirs[dir][0]>=0 and y+dirs[dir][1]>=0 and encode[x+dirs[dir][0]][y+dirs[dir][1]]==2 :
        x+=dirs[dir][0]
        y+=dirs[dir][1]
    else:
        dir+=1
        dir=dir%4
        x+=dirs[dir][0]
        y+=dirs[dir][1]
for i in range(R):
    for j in range(C):
        print(encode[i][j],end="")




