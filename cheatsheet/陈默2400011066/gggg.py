import heapq
n=int(input())
lst=[]
for i in range(n):
    l=int(input())
    lst.append(l)
heapq.heapify(lst)
total=0
while len(lst)>1:
    a=heapq.heappop(lst)
    b=heapq.heappop(lst)
    total+=a+b
    heapq.heappush(lst,a+b)
print(total)