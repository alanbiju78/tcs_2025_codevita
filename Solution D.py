N,M=map(int,input().split())
grid=[input().strip().split() for _ in range(N)]
x,y=map(int,input().split())
prl,plt,gld,dia=map(int,input().split())
K=int(input())

values={'$':prl,'*':plt,'%':gld,'+':dia}

def stable(i,j):
    return i==N-1 or grid[i+1][j]=='#'
max_score=0

def dfs(i,j,moves,score,visited):

    global max_score
    if moves>K:
        return
    if stable(i,j) and i!=N-1:
        max_score=max(max_score,score)

    for dj in [-1,1]:
        nj=j+dj
        if 0<=nj < M and grid[i][nj]!='#' and (i,nj) not in visited:
            ni,nscore,nmoves=i,score+values[grid[i][nj]],moves+1
            path = [(ni, nj)]
            
            while ni+1<N and grid[ni+1][nj]!='#' and not stable(ni,nj) and nmoves<K:
                ni+=1
                nscore+=values[grid[ni][nj]]
                nmoves+=1
                path.append((ni,nj))
            
            for cell in path:
                visited.add(cell)
            dfs(ni,nj,nmoves,nscore,visited)
            for cell in path:
                visited.remove(cell)

    if moves+1<=K and i-2>=0 and grid[i-1][j]=='#' and grid[i-2][j]!='#' and (i-2,j) not in visited:
        ni,nj=i-2,j
        nscore=score+values[grid[ni][nj]] 
        visited.add((ni,nj))
        dfs(ni,nj,moves+1,nscore,visited)
        visited.remove((ni,nj))

visited={(x, y)}
initial_score=values[grid[x][y]]
if stable(x,y) and x!=N-1:
    max_score=initial_score
dfs(x,y,0,initial_score,visited)
print(max_score)