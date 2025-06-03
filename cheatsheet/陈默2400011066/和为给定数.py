def binarysearch(lst,sta,target):
    start = sta
    end = len(lst)-1
    while start <= end:
        mid = (start+end)//2
        if lst[mid] == target:
            return True
        if lst[mid] > target:
            end = mid - 1
        if lst[mid] < target:
            start = mid + 1
    return False
n=int(input())
lst=list(map(int,input().split()))
m=int(input())
lst.sort()
find=False
for i in range(n):
    if lst[i]>m/2:
        break
    if binarysearch(lst,i+1,m-lst[i]):
        find=True
        print(lst[i],m-lst[i])
        break
if not find:
    print('No')
#不要反复给列表切片，很费时间