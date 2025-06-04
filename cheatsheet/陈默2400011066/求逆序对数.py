import bisect
def antiorder(lst):
    a=[]
    ans=0
    for i in lst:
        ind=bisect.bisect_left(a,i)
        bisect.insort(a,i)
        ans+=ind
    return ans
while True:
    n=int(input())
    if n==0:
        break
    lst=list(map(int,input().split()))
    print(antiorder(lst[::-1]))
