mat1=[[x for x in input().split()] for i in range(9)]
hint = [int(x) for x in input().split()]
k=int(input())
kcnt=0
print(mat1)
print(hint)
print(k)
checkrowls=[]
posls=[]
checkcolls=[]

def checkrow(mat1, i):
    for j in range(9):
        checkrowls.append(mat1[i][j].strip('0'))
    for j in range(9):
        if mat1[i][j] in checkrowls:
            return checkcol(mat1, j)

def checkcol(mat1, j):
    for i in range(9):
        checkcolls.append(mat1[i][j].strip('0'))
    for i in range(9):
        if mat1[i][j] in checkcolls:
            return str(i) + str(j)
for i in range(9):
    for j in range(9):
        if mat1[i][j].startswith('0'):
            pos=checkrow(mat1,i)
            posls.append(pos)
            kcnt+=1
    checkrowls=[]
    checkcolls=[]
    if kcnt > k:
        print("Impossible")
        exit()
if kcnt ==0:
    print("Won")
elif kcnt < k:
    print(*posls, sep='\n')

            