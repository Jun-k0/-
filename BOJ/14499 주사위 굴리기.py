import sys

input=sys.stdin.readline

dx=[1,-1,0,0]
dy=[0,0,-1,1]

dice=[0]*6

n,m,y,x,k=map(int,input().split())
board=[]
for i in range(n):
    board.append(list(map(int,input().split())))

inst=list(map(int,input().split()))

# 굴릴 때 상태를 저장해놈, now와 반대면을 고정하고 시작
def rotate(dirr):
    if dirr==1:
        dice[1],dice[5],dice[2],dice[0]=dice[0],dice[1],dice[5],dice[2]
    elif dirr==2:
        dice[2],dice[0],dice[1],dice[5]=dice[0],dice[1],dice[5],dice[2]
    elif dirr==3:
        dice[3],dice[4],dice[0],dice[5]=dice[0],dice[5],dice[4],dice[3]
    else:
        dice[4],dice[0],dice[3],dice[5]=dice[0],dice[3],dice[5],dice[4]

for i in inst:
    x+=dx[i-1]
    y+=dy[i-1]
    if x>=0 and y>=0 and x<m and y<n:
        rotate(i)
        if board[y][x]==0:
            board[y][x]=dice[0]
        else:
            dice[0]=board[y][x]
            board[y][x]=0
        print(dice[5])
    else:
        x-=dx[i-1]
        y-=dy[i-1]
        
'''
미리 구현 끝내고 코딩하기
'''
