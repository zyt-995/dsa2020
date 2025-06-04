def convert(postord,inord):
    if not postord:
        return ""
    if len(postord)==1:
        return postord
    ind=inord.index(postord[0])
    return convert(postord[1:ind+1],inord[:ind])+convert(postord[ind+1:],inord[ind+1:])+postord[0]
import sys
for line in sys.stdin:
    line = line.strip()
    if line=="EOF":
        break
    s1,s2=map(str,line.split())
    print(convert(s1,s2))