s=input()
dict={}
for i in s:
    if i not in dict:
        dict[i]=1
    else:
        dict[i]+=1
ind=float("inf")
for k,v in dict.items():
    if v==1:
        temp=s.index(k)
        ind=min(ind,temp)
if ind!=float("inf"):
    print(ind)
else:
    print(-1)