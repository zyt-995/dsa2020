import bisect
n=int(input())
lst=list(map(int,input().split()))
count=0
temp=[]
for i in lst[::-1]:
    index=bisect.bisect_left(temp,i)
    bisect.insort(temp,i)
    count+=index
print(count)