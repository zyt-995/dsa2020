def sort(a):
    if len(a)<=1:
        return 0,a
    mid=len(a)//2
    lcount,left=sort(a[:mid])
    rcount,right=sort(a[mid:])
    count=lcount+rcount
    answer=[]
    while left and right:
        if left[0]>right[0]:
            count=count+len(right)
            answer.append(left.pop(0))
        else:
            answer.append(right.pop(0))
    if left==[]:
        answer.extend(right)
    if right==[]:
        answer.extend(left)
    return count,answer
while True:
    try:
        n=int(input())
        if n==0:
            break
        a=list(map(int,input().split()))
        flag,_=sort(a)
        print(flag)
    except :
        break
