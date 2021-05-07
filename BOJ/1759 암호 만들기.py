import sys

input=sys.stdin.readline

n,m=map(int,input().split())
arr=input().split()
arr.sort()
ans=[]

mo=['a','e','i','o','u']
now_mo=0
now_za=0

def sol(cnt,idx):
    global now_mo,now_za
    if cnt==n:
        if now_mo>=1 and now_za>=2:
            for i in ans:
                print(i,end="")
            print()
    else:
        for i in range(idx,m):
            if arr[i] in mo:
                now_mo+=1
                ans.append(arr[i])
                sol(cnt+1,i+1)
                temp=ans.pop()
                now_mo-=1
            else:
                now_za+=1
                ans.append(arr[i])
                sol(cnt+1,i+1)
                temp=ans.pop()
                now_za-=1
            
sol(0,0)
'''
증가하는 순 visit 필요 없음
'''
