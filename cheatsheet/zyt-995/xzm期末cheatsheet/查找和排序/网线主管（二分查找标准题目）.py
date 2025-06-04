n,k=map(int,input().split())
a=[]
for _ in range(n):
    num=float(input())
    a.append(int(num*100))
right=sum(a)//k
if right==0:
    print('0.00')
    exit()
left=0
def valid(mid):
    count=0
    for i in range(n):
        num=a[i]//mid
        count+=num
    if count>=k:
        return True
    else:
        return False
while left<=right:
    mid=(right+left)//2
    if valid(mid):
        prev=mid
        left=mid+1
    else:
        right=mid-1
prev=prev/100
print('%.2f' %prev,end=' ')
print('%.4f' %prev)