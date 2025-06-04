ini=input()
while True:
    try:
        seq=input()
        stack=[]
        inicurr=0
        seqcurr=0
        while seqcurr<len(seq):
           while ini[inicurr]!=seq[seqcurr] and inicurr<len(seq)-1:
                stack.append(ini[inicurr])
                inicurr+=1
           seqcurr+=1
        if stack:
            print("NO")
        else:
            print("YES")
    except:
        break