import sys
from collections import deque
input=sys.stdin.readline

n=int(input())
k=int(input())
board=[[0]*n for _ in range(n)]
for i in range(k):
    a,b = map(int, input().split())
    board[a-1][b-1]=1

rot=[]
l=int(input())
for i in range(l):
    a,b=input().split()
    rot.append((int(a),b))

dx=[1,0,-1,0]
dy=[0,1,0,-1]
time=0
dir=0
idx=0
now=deque()
now.append((0,0))
while True:
    x=now[0][0]
    y=now[0][1]
    
    if idx<len(rot):
        if time==rot[idx][0]:
            if rot[idx][1]=='L':
                dir-=1
            else:
                dir+=1
            if dir>3:
                dir-=4
            elif dir<0:
                dir+=4
            idx+=1
        
    nx=x+dx[dir]
    ny=y+dy[dir]
    if (nx>=0 and ny>=0 and nx<n and ny<n) and (nx,ny) not in now:
        if board[ny][nx]==1:
            now.appendleft((nx,ny)) # 머리를 앞으로
            board[ny][nx]=0
        else:
            now.appendleft((nx,ny))
            temp=now.pop()
        time+=1
    else:
        time+=1
        break
print(time)

'''
구현 문제 - 지문 전체 읽기
'''
