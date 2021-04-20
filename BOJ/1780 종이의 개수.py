import sys

input=sys.stdin.readline

n=int(input())
arr=[]
ans=[0,0,0]
for _ in range(n):
    arr.append(list(map(int,input().split())))

def sol(n,x1,y1,x2,y2):               # x2 y2 필요없을듯
    if n==1:
        ans[arr[y1][x1]+1]+=1
        return
    chk=True
    for i in range(y1,y2):
        if chk==False:
            break
        for j in range(x1,x2):
            if arr[i][j]!=arr[y1][x1]:
                chk=False 
                div=n//3
                for k in range(3):
                    for l in range(3):
                        sol(div,x1+k*div,y1+l*div,x1+(k+1)*div,y1+(l+1)*div) # 분할하는거 반복문으로 줄일 수 있음
                break # return 해서 chk 필요 없게
    if chk:
        ans[arr[y1][x1]+1]+=1
        
sol(n,0,0,n,n)
for i in ans:
    print(i)
