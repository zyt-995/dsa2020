import bisect
n=int(input())
lst=list(map(int,input().split()))
k=int(input())
ans=[]
for i in lst:
    bisect.insort(ans, i)
for i in range(n-1,n-k-1,-1):
    print(ans[i])