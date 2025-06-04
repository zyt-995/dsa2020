def move(A,B,C,n):
    if n==1:
        return [f"{A}->{C}"]
    else:
        return move(A,C,B,n-1)+[f"{A}->{C}"]+move(B,A,C,n-1)
n=int(input())
lst=move("A","B","C",n)
for i in lst:
    print(i)
