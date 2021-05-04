import sys
from collections import deque

input=sys.stdin.readline

arr=[]
n,m=map(int,input().split())
for _ in range(m):
    arr.append(input().rstrip())

dist=[[-1]*n for _ in range(m)]
dx=[1,0,-1,0]
dy=[0,1,0,-1]

def bfs():
    q=deque()
    q.append((0,0))
    dist[0][0]=0
    while q:
        now=q.popleft()
        x=now[0]
        y=now[1]
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx>=0 and nx<n and ny>=0 and ny<m:
                if dist[ny][nx]==-1:
                    if arr[ny][nx]=='1':
                        dist[ny][nx]=dist[y][x]+1
                        q.append((nx,ny))
                    else:
                        dist[ny][nx]=dist[y][x]
                        q.appendleft((nx,ny))

bfs()
print(dist[m-1][n-1])

'''
최단거리(가중치 방식) + 다익스트라(가중치 넣어서 heapq)
이 문제는 pq필요없이 deque로만 해결함
'''
