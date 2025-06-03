#每次都合并最少的两个堆
import heapq
n=int(input())
a=list(map(int,input().split()))
heapq.heapify(a)
total=0
while len(a)>1:
    x=heapq.heappop(a)
    y=heapq.heappop(a)
    total+=x+y
    heapq.heappush(a,x+y)
print(total)