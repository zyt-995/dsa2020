import heapq
n=int(input())
lst=list(map(int,input().split()))
heapq.heapify(lst)
ans=0
while len(lst)>1:
    a=heapq.heappop(lst)
    b=heapq.heappop(lst)
    ans+=a+b
    heapq.heappush(lst,a+b)
print(ans)

