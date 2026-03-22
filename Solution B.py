digit=input()
dir_seq=input()
dict1={
    ((1,),(1,1),(0,),(1,1),(1,)):0,
    ((0,),(0,1),(0,),(0,1),(0,)):1,
    ((1,),(0,1),(1,),(1,0),(1,)):2,
    ((1,),(0,1),(1,),(0,1),(1,)):3,
    ((0,),(1,1),(1,),(0,1),(0,)):4,
    ((1,),(1,0),(1,),(0,1),(1,)):5,
    ((1,),(1,0),(1,),(1,1),(1,)):6,
    ((1,),(0,1),(0,),(0,1),(0,)):7,
    ((1,),(1,1),(1,),(1,1),(1,)):8,
    ((1,),(1,1),(1,),(0,1),(1,)):9
}
dict1_inv={v:k for k,v in dict1.items()}
dict1[((0,), (1,0), (0,), (1,0), (0,))]=1

lst1=[]

def convert(digit,dir_seq):
    befmir=dict1_inv[int(digit)]
    if dir_seq=='U' or dir_seq=='D':
        aftmir=befmir[::-1]
        
    elif dir_seq=='L' or dir_seq=='R':
        aftmir=tuple(tuple(row[::-1]) for row in befmir)
        
    elif dir_seq=='N' or dir_seq=='S':
        aftmir=befmir

    return dict1.get(aftmir)

for i in range(len(digit)):
    char=convert(digit[i],dir_seq[i])
    if char is not None:
        lst1.append(int(char))
lst1.sort()
out=int(''.join(map(str,lst1)))
print(out)     