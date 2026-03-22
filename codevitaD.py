stringlist=[x for x in input().split()]
#print(stringlist)
flag=0
newlist=[]
dict1={"add": "+", "sub": "-", "mul": "*", "rem": "%", "pow": "**"}
dict2={"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9, "zero": 0}
for i in range(len(stringlist)):
    if stringlist[i] in dict1:
        newlist.append(dict1[stringlist[i]])
    elif stringlist[i] in dict2:
        newlist.append(dict2[stringlist[i]])
    else:
        l1=len(stringlist[i])
        for j in range(l1):
            if (stringlist[i][j] == 'c') and (stringlist[i][j+1:l1:1] in dict2) and (stringlist[i][0:j:1] in dict2):
                
                
                sum1=dict2[stringlist[i][0:j:1]]
                sum1=sum1*10+dict2[stringlist[i][j+1:l1:1]]
                flag=1
                break
        if flag==0:
            print("expression evaluation stopped invalid words present")
            exit()
        else:
            newlist.append(sum1)
#print(newlist)
finallist=[]
finalcnt=0
valid=0
for i in range(len(newlist)):
    if type(newlist[i]) == str:
        finallist.append(newlist[i])
        finalcnt+=1
    elif type(newlist[i]) == int:
        if str(finallist[finalcnt-1]) in "+-*%**" and type(newlist[i+1]) == int:
            if finallist[finalcnt-1] == '+':
                finallist[finalcnt-1]=newlist[i]+newlist[i+1]
            elif finallist[finalcnt-1] == '-':
                finallist[finalcnt-1]=newlist[i]-newlist[i+1]
            elif finallist[finalcnt-1] == '*':
                finallist[finalcnt-1]=newlist[i]*newlist[i+1]
            elif finallist[finalcnt-1] == '%':
                finallist[finalcnt-1]=newlist[i]%newlist[i+1]
            elif finallist[finalcnt-1] == '**':
                finallist[finalcnt-1]=newlist[i]**newlist[i+1]
            i+=2
        elif finallist[finalcnt-1] in dict2.values():
            if finallist[finalcnt-2] == '+':
                finallist[finalcnt-2]= finallist[finalcnt-1]+newlist[i]
            elif finallist[finalcnt-2] == '-':
                finallist[finalcnt-2]= finallist[finalcnt-1]-newlist[i]
            elif finallist[finalcnt-2] == '*':
                finallist[finalcnt-2]= finallist[finalcnt-1]*newlist[i]
            elif finallist[finalcnt-2] == '%':
                finallist[finalcnt-2]= finallist[finalcnt-1]%newlist[i]
            elif finallist[finalcnt-2] == '**':
                finallist[finalcnt-2]= finallist[finalcnt-1]**newlist[i]
            finalcnt-=1
            finallist.pop()
print(finallist[0])
            
        