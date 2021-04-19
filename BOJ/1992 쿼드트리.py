import sys

input=sys.stdin.readline

n=int(input())
arr=[]
ans=[]
for _ in range(n):
    arr.append(input().rstrip())

def sol(n,x1,y1,x2,y2):
    if n==1:
        ans.append(arr[y1][x1])
    else:
        chk=True
        for i in range(y1,y2):
            if chk==False:
                break
            for j in range(x1,x2):
                if arr[i][j]!=arr[y1][x1]:
                    chk=False
                    ans.append('(')
                    mid=n//2
                    sol(mid, x1, y1, x1+mid, y1+mid) ## 각각의 +하는 순서 기억해놓자
                    sol(mid, x1+mid, y1, x2, y1+mid)
                    sol(mid, x1, y1+mid, x1+mid, y2)
                    sol(mid, x1+mid, y1+mid, x2, y2)
                    ans.append(')')
                    break
        if chk:
            ans.append(arr[y1][x1])

sol(n,0,0,n,n)
for i in ans:
    print(i,end="")
    
'''
/ 하면 무조건 실수형이 됨 //로 ㄱㄱ
분할하는 점들은 나누지 말고 더하기
분할정복 감 더 익히기
'''
