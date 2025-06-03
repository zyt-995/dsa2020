n=int(input())
max=0
min=float("inf")
total=0
for i in range(n):
    count=float(input())
    if count>max:
        max=count
    if count<min:
        min=count
    total+=count
ans=(total-max-min)/(n-2)
print(f"{ans:.2f}")
