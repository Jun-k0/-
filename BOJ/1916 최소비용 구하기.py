import sys
import heapq

input=sys.stdin.readline

n=int(input())
m=int(input())
graph=[[] for _ in range(n+1)]
for _ in range(m):
    a,b,cost=map(int,input().split())
    graph[a].append((cost,b))
s,e=map(int,input().split())

INF=int(1e9)
d=[INF]*(n+1)
d[s]=0

def dijkstra(s):
    q=[]
    heapq.heappush(q,(0,s))
    while q:
        temp=heapq.heappop(q)
        now=temp[1]
        cost=temp[0]
        for i in graph[now]:
            if d[i[1]]>cost+i[0]:
                d[i[1]]=cost+i[0]
                heapq.heappush(q,(d[i[1]],i[1]))
                
dijkstra(s)
print(d[e])
