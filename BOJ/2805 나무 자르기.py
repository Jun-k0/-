import sys

input=sys.stdin.readline

n,m=map(int,input().split())
arr=list(map(int,input().split()))
arr.sort()

s=0
e=arr[-1]
ans=0
while s<=e:
    mid=(s+e)//2
    tree=0
    for i in arr:
        if mid<i:
            tree+=i-mid
    if tree<m:
        e=mid-1
    elif tree==m:
        ans=mid
        break
    else:
        ans=mid     # 최대한 덜 잘라야 하므로
        s=mid+1
print(ans)
'''
입력 범위가 큼 lg n 필요
'''
