
directions=[(-1,0),(0,1),(1,0),(0,-1)]
def simulate(i,j,seq,dir_index):
    for move in seq:
        if move=='S':
            di,dj =directions[dir_index]
            i+=di
            j+=dj
            if not(0<=i<R and 0<=j<C) or city_map[i][j]=='#':
                return False
        elif move=='L':
            dir_index=(dir_index-1)%4
        elif move=='R':
            dir_index=(dir_index+1)%4
    return True


R,C=map(int,input().split())
city_map=[list(input().strip()) for _ in range(R)]
movement_sequence=input().strip()

count = 0
for i in range(R):
    for j in range(C):
        if city_map[i][j]=='#':
            continue
        for d in range(4):
            if simulate(i,j,movement_sequence,d):
                count+=1
print(count)
