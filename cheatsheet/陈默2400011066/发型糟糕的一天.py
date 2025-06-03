n=int(input())
height=[]
for i in range(n):
    height.append(int(input()))
stack=[]
count=0
for i in range(n-1,-1,-1):
    while stack and height[stack[-1]]<height[i]:
        stack.pop()
    if not stack:
        j=n
    else:
        j=stack[-1]
    count+=(j-i-1)
    stack.append(i)
print(count)