stringlist = [x for x in input().split()]
flag = 0
newlist = []
dict1 = {"add": "+", "sub": "-", "mul": "*", "rem": "%", "pow": "**"}
dict2 = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9, "zero": 0 }

for i in range(len(stringlist)):
    if stringlist[i] in dict1:
        newlist.append(dict1[stringlist[i]])
    elif stringlist[i] in dict2:
        newlist.append(dict2[stringlist[i]])
    else:
        l1 = len(stringlist[i])
        flag = 0
        parts = stringlist[i].split('c')
        if all(part in dict2 for part in parts):
            sum1 = 0
            for part in parts:
                sum1 = sum1 * 10 + dict2[part]
            flag = 1
        if flag == 0:
            print("expression evaluation stopped invalid words present")
            exit()
        else:
            newlist.append(sum1)

# print("Parsed newlist:", newlist)

finallist = []
finalcnt = 0

def evaluate_prefix(index):
    if index[0]>=len(newlist):
        print("expression is not complete or invalid")
        exit()
    token = newlist[index[0]]
    index[0] += 1
    if type(token)==str:
        left = evaluate_prefix(index)
        right = evaluate_prefix(index)
        if token=='+':
            return left+right
        elif token=='-':
            return left-right
        elif token=='*':
            return left*right
        elif token=='%':
            return left%right
        elif token=='**':
            return left**right
    elif type(token)==int:
        return token
    else:
        print("expression is not complete or invalid")
        exit()

index = [0]
result = evaluate_prefix(index)
if index[0]!=len(newlist):
    print("expression is not complete or invalid")
else:
    print(result)
