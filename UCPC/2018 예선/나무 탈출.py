import sys
input=sys.stdin.readline
from collections import deque
#sys.setrecursionlimit(10**6)

n=int(input())
graph=[[] for _ in range(n+1)]
for i in range(n-1):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

ans=0
q=deque()
q.append((1,0))
visit=[False]*(n+1)
visit[1]=True

def bfs():
    global ans
    while q:
        p=q.popleft()
        if p[0]!=1 and len(graph[p[0]])==1:
            ans+=p[1]
        for i in graph[p[0]]:
            if not visit[i]:
                visit[i]=True
                q.append((i,p[1]+1))
bfs()

if ans%2==0:
    print("No")
else:
    print("Yes")
    
'''
루트에서 리프까지 중복하여 총 간선 수를 세면 되는 문제다.
처음에 DFS로 했다가 파이썬의 재귀 에러에 빠져서 BFS로 고쳐서 해결함.
재귀 에러 해결을 위해 sys.setrecursionlimit(10**6)을 해도 메모리 초과가 나버리므로
웬만하면 반복문쪽으로 ㄱㄱ
'''
