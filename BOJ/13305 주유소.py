import sys

input=sys.stdin.readline

n=int(input())
dist=list(map(int,input().split()))
cost=list(map(int,input().split()))

minn=cost[0]
ans=0
for i in range(n-1):
    ans+=minn*dist[i]
    if cost[i+1]<minn:
        minn=cost[i+1]
print(ans)
