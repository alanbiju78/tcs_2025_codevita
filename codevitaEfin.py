mat1=[[x for x in input().split()]for i in range(9)]
hint=[int(x) for x in input().split()]
k=int(input())

kcnt=0
checkrowls=[]
checkcolls=[]
posls=[]

def checkrow(mat1,i):
    checkrowls.clear()
    for j in range(9):
        checkrowls.append(mat1[i][j].lstrip('0'))
    for j in range(9):
        if checkrowls.count(mat1[i][j].lstrip('0'))>1:
            return checkcol(mat1,j)

def checkcol(mat1,j):
    checkcolls.clear()
    for i in range(9):
        checkcolls.append(mat1[i][j].lstrip('0'))
    for i in range(9):
        if checkcolls.count(mat1[i][j].lstrip('0'))>1:
            return f"{i} {j}"

for i in range(9):
    for j in range(9):
        if mat1[i][j].startswith('0'):
            pos=checkrow(mat1,i)
            if pos:
                posls.append(pos)
                kcnt+=1
    if kcnt>k:
        print("Impossible")
        exit()

if kcnt==0:
    print("Won")
elif kcnt<k:
    print('\n'.join(posls))
