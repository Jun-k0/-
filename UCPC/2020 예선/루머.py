import sys
from collections import deque
input=sys.stdin.readline

n=int(input())

answer=[-1]*n
graph=[]
graph.append([-1])

for i in range(n):
    arr=list(map(int,input().split()))
    arr.pop()
    graph.append(arr)
    
s=int(input())
rumor=deque()
start=list(map(int,input().split()))
for i in start:
    answer[i-1]=0
    rumor.append((i,0))

def bfs():
    while rumor:
        spread=rumor.popleft()
        if answer[spread[0]-1]==-1:
            answer[spread[0]-1]=spread[1]
        for i in graph[spread[0]]:
            if answer[i-1]>-1:
                continue
            chk_trust=0
            for j in graph[i]:
                if answer[j-1]==-1:
                    chk_trust-=1
                else:
                    chk_trust+=1
            if chk_trust>=0:
                rumor.append((i,spread[1]+1))
                # answer[i-1]=spread[1]+1

bfs()
for i in answer:
    print(i,end=" ")

# 조건 맞게 bfs
