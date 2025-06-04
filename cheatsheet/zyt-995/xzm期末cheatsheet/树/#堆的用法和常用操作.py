#堆的用法和常用操作
import heapq
#heapq.heapify(a):复杂度 O（logn）
#heapq.heappush(s,item):往已经是堆的列表s里面添加元素item
#heapq.heappop(s) 取出并返回堆顶元素。s必须已经是个堆(注意：会减少s长度)
#heapq.heapreplace(s,item) 取出并返回堆顶元素,并将元素item加入堆(s还是个堆，长度不变)
#heapq.nlargest(n,s,key) 返回序列s中的最大n个元素构成的列表。key是关键字函数
#heapq.nsmallest(n,s,key) 返回最大的n个元素
print(heapq.nlargest(3,a,lambda x:x%10)) #返回函数的用法
