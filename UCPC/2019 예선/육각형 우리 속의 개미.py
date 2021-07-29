import sys
input=sys.stdin.readline

n=int(input())
if n<5:
    print("0")
    exit()
# graph=[[] for _ in range(50)]
visit=[[False]*50 for _ in range(50)]

ans=0        

def dfs(x,y,cnt,dirr):
    if cnt==n+1:
        return
    global ans
    if dirr==0:
        x+=1
        y-=1
        if visit[y][x]==True and n==cnt+1:
            ans+=1
        elif visit[y][x]==False:
            visit[y][x]=True
            dfs(x,y,cnt+1,2)
            dfs(x,y,cnt+1,5)
            visit[y][x]=False
    elif dirr==1:
        x-=1
        y-=1
        if visit[y][x]==True and n==cnt+1:
            ans+=1
        elif visit[y][x]==False:
            visit[y][x]=True
            dfs(x,y,cnt+1,2)
            dfs(x,y,cnt+1,4)
            visit[y][x]=False
    elif dirr==2:
        y-=1
        if visit[y][x]==True and n==cnt+1:
            ans+=1
        elif visit[y][x]==False:
            visit[y][x]=True
            dfs(x,y,cnt+1,0)
            dfs(x,y,cnt+1,1)
            visit[y][x]=False
    elif dirr==3:
        y+=1
        if visit[y][x]==True and n==cnt+1:
            ans+=1
        elif visit[y][x]==False:
            visit[y][x]=True
            dfs(x,y,cnt+1,4)
            dfs(x,y,cnt+1,5)
            visit[y][x]=False
    elif dirr==4:
        x-=1
        y+=1
        if visit[y][x]==True and n==cnt+1:
            ans+=1
        elif visit[y][x]==False:
            visit[y][x]=True
            dfs(x,y,cnt+1,3)
            dfs(x,y,cnt+1,1)
            visit[y][x]=False
    elif dirr==5:
        x+=1
        y+=1
        if visit[y][x]==True and n==cnt+1:
            ans+=1
        elif visit[y][x]==False:
            visit[y][x]=True
            dfs(x,y,cnt+1,3)
            dfs(x,y,cnt+1,0)
            visit[y][x]=False

visit[26][25]=True
dfs(25,26,-1,2)

print(ans)

'''
2^21승 돌리면 4백만이므로 완탐 DFS
'''
