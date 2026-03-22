stringx=input()
stringy=input()
if not all(char in stringy for char in set(stringx)):
    print("Impossible")
    exit()

revstringy=stringy[::-1]
sum1=0
srlist=[int(x) for x in input().split()]
if srlist[0]>srlist[1]:
    gn=srlist[0]
    ln=srlist[1]
    gstring=stringy
    lstring=revstringy
elif srlist[0]<srlist[1]:
    gn=srlist[1]
    ln=srlist[0]
    gstring=revstringy
    lstring=stringy
else:
    gn=srlist[0]
    ln=srlist[1]
    gstring=stringy
    lstring=revstringy

stringxsubs=set()
for i in range(len(stringx)):
    for j in range(i+1,len(stringx)+1):
        sub=stringx[i:j]
        stringxsubs.add(sub)

gstringsubs=set()
for i in range(len(gstring)):
    for j in range(i+1,len(gstring)+1):
        sub=gstring[i:j]
        gstringsubs.add(sub)

lstringsubs=set()
for i in range(len(lstring)):
    for j in range(i+1,len(lstring)+1):
        sub=lstring[i:j]
        lstringsubs.add(sub)

visited=set()
sorted_stringxsubs=sorted(stringxsubs,key=lambda x:-len(x))
for key in sorted_stringxsubs:
    if key in visited:
        continue
    if key in lstringsubs:
        for i in range(len(key)):
            for j in range(i+1,len(key)+1):
                sub=key[i:j]
                visited.add(sub)
        sum1+=ln
    elif key in gstringsubs:
        for i in range(len(key)):
            for j in range(i+1,len(key)+1):
                sub=key[i:j]
                visited.add(sub)
        sum1+=gn
print(sum1)
