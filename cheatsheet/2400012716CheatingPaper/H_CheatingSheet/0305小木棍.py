'''
250305:小木棍
查看提交统计提问
总时间限制: 2000ms 内存限制: 65536kB
描述
小明将一批等长的木棍随机切成最长为50单位的小段。现在他想要将木棍还原成原来的状态，但是却忘记了原来的木棍数量和长度。请写一个程序帮助他计算如果还原成原来的等长木棍，其长度可能的最小值。所有的长度均大于0。

输入
输入包含多个实例。每个实例有两行，第一行是切割后的木棍数量n（最多64个），第二行为n个以空格分开的整数，分别为每根木棍的长度。输入的最后以n为 0 结束。
输出
对于每个实例，输出一行其长度的可能的最小值。
样例输入
9
5 2 1 5 2 1 5 2 1
4
1 2 3 4
0
样例输出
6
5
'''

def check_division(sticks_length,length,num_of_sticks,current_length):
    s=sticks_length
    current_length%=length
    if num_of_sticks==0 and current_length==0:
        return True
    elif num_of_sticks==0 and current_length:
        return False
    else:
        if s[-1]>length-current_length:
            return False
        if current_length==0:
            current_length+=s[0]
            return check_division(s[1:],length,num_of_sticks-1,current_length)
        else:
            res=False
            prev=-1
            for i in range(num_of_sticks) :
                if s[i]+current_length<=length and s[i]!=prev and res==False:
                    m=[s[t] for t in range(num_of_sticks) if t!=i]
                    res=res or check_division(m,length,num_of_sticks-1,current_length+s[i])
            return res




while True:
    n=int(input())
    if n==0:
        break
    else:
        sticks=list(map(int,input().split()))
        total_len=sum(sticks)
        sticks.sort(reverse=1)
        for length in range(sticks[0],total_len+1):
            if total_len%length:
                continue
            if check_division(sticks,length,n,0):
                print(length)
                break






