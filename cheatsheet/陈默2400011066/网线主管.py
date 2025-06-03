n,k=map(int,input().split())
lines=[]
for i in range(n):
    l=float(input())
    lines.append(round(l*100))
def isok(target):
    ans=0
    for i in lines:
        ans+=i//target
    return ans
start=0
end=max(lines)
while start<end:
    mid=(start+end+1)//2
    if isok(mid)>=k:
        start=mid
    else:
        end=mid-1
if start!=0:
    print(f"{start/100:.2f}")
else:
    print("0.00")

