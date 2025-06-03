import bisect
n=int(input())
speed=list(map(int,input().split()))
lst=[]
count=0
for i in speed:
    ind=bisect.bisect_left(lst,i)
    bisect.insort(lst,i)#别忘记这一行
    count+=ind
print(count)