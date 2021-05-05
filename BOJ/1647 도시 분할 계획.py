import sys

input=sys.stdin.readline

n,m=map(int,input().split())
arr=[]
for _ in range(m):
    a,b,c=map(int,input().split())
    arr.append((c,a,b))
arr.sort()
ans=0
temp=0
parent=[0]*(n+1)
for i in range(1,n+1):
    parent[i]=i
    
def findp(n):
    if parent[n]!=n:
        parent[n]=findp(parent[n])  # return findp(parent) 와 차이
    return parent[n]
def union(a,b):
    a=findp(a)
    b=findp(b)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b
    
for i in arr:
    if findp(i[1])!=findp(i[2]):
        temp=i[0]
        ans+=i[0]
        union(i[1],i[2])

print(ans-temp)
