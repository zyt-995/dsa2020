a=list(map(int,input().split()))
l=len(a)
jishu,oushu,answer=[],[],[]
for i in range(l):
    if a[i]%2==0:
        oushu.append(a[i])
    else:
        jishu.append(a[i])
oushu=sorted(oushu,reverse=False)
jishu=sorted(jishu,reverse=True)
answer=jishu+oushu
for j in range(l):
    print(answer[j],end=' ')
