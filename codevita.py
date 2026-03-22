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

stringxdict={}
for i in range(len(stringx)):
    for j in range(i+1,len(stringx)+1):
        sub=stringx[i:j]
        stringxdict[sub]=0

gstringdict={}
for i in range(len(gstring)):
    for j in range(i+1,len(gstring)+1):
        sub=gstring[i:j]
        gstringdict[sub]=0
lstringdict={}
for i in range(len(lstring)):
    for j in range(i+1,len(lstring)+1):
        sub=lstring[i:j]
        lstringdict[sub]=0

sorted_stringxdict=sorted(stringxdict.keys(),key=lambda x:-len(x))
for key in sorted_stringxdict:
    if lstringdict.get(key,0)==1:
        for i in range(len(key)):
            for j in range(i+1,len(key)+1):
                sub = key[i:j]
                if sub in stringxdict:
                    stringxdict[sub] = 1
                lstringdict[sub] = 1
                gstringdict[sub] = 1
    
        sum1+=ln
    elif gstringdict.get(key,0) == 1:
        for i in range(len(key)):
            for j in range(i+1,len(key)+1):
                sub=key[i:j]
                if sub in stringxdict:
                    stringxdict[sub] = 1
                gstringdict[sub] = 1
                lstringdict[sub] = 1   
        sum1+=gn
print(sum1)
