import sys

input=sys.stdin.readline

n=int(input())
visit=[False]*(n+1)
arr=[]

def sol(cnt):
    if cnt==n:
        for i in arr:
            print(i,end=" ")
        print()
    else:
        for i in range(1,n+1):
            if not visit[i]:
                arr.append(i)
                visit[i]=True
                sol(cnt+1)
                visit[i]=False
                temp=arr.pop()

sol(0)
