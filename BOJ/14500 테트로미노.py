import sys

input=sys.stdin.readline

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
tetromino = [
    [(0,0), (0,1), (1,0), (1,1)],
    [(0,0), (0,1), (0,2), (0,3)],
    [(0,0), (1,0), (2,0), (3,0)],
    [(0,0), (0,1), (0,2), (1,0)], 
    [(1,0), (1,1), (1,2), (0,2)],
    [(0,0), (1,0), (1,1), (1,2)],
    [(0,0), (0,1), (0,2), (1,2)],
    [(0,0), (1,0), (2,0), (2,1)],
    [(2,0), (2,1), (1,1), (0,1)],
    [(0,0), (0,1), (1,0), (2,0)], 
    [(0,0), (0,1), (1,1), (2,1)],
    [(0,0), (0,1), (0,2), (1,1)],
    [(1,0), (1,1), (1,2), (0,1)],
    [(0,0), (1,0), (2,0), (1,1)],
    [(1,0), (0,1), (1,1), (2,1)],
    [(1,0), (2,0), (0,1), (1,1)],
    [(0,0), (1,0), (1,1), (2,1)],
    [(1,0), (0,1), (1,1), (0,2)],
    [(0,0), (0,1), (1,1), (1,2)]
]

ans=0
def sol(x, y):
    global ans
    for i in range(19):
        result = 0
        for j in range(4):
            try:        # try문 예외처리
                ny = y+tetromino[i][j][0]
                nx = x+tetromino[i][j][1]
                result += board[ny][nx]
            except:
                continue
        ans = max(ans, result)
        

for i in range (n):
    for j in range(m):
        sol(j,i)

print(ans)

# DFS로 풀면 ㅗ 모양이 안나옴 
'''
import sys

input=sys.stdin.readline

arr=[]
n,m=map(int,input().split())
for i in range(n):
    arr.append(list(map(int,input().split())))

visit=[[False]*(m) for _ in range(n)]
dx=[1,0,-1,0]
dy=[0,1,0,-1]
ans=0
def dfs(x,y,cnt,val):
    global ans
    if cnt==4:
        ans=max(ans,val)
    else:
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx>=0 and nx<m and ny>=0 and ny<n:
                if not visit[ny][nx]:
                    visit[ny][nx]=True
                    dfs(nx,ny,cnt+1,val+arr[ny][nx])
                    visit[ny][nx]=False

for i in range(n):
    for j in range(m):
        visit[i][j]=True
        dfs(j,i,1,arr[i][j])
print(ans)
'''
