import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline

n,r,c=map(int,input().split())
res=0

def sol(x, y, n):
    global res
    if x == r and y == c:
        print(res)
        exit(0)
    elif n == 1:
        res += 1
        return
    if not (x <= r < x + n) and not (y <= c < y + n):
        res += n ** 2
        return
    mid=n//2
    sol(x, y, mid)
    sol(x, y + mid, mid)
    sol(x + mid, y, mid)
    sol(x + mid, y + mid, mid)

sol(0,0,2**n)
print(res)

# [2**n][2**n]의 2차원 배열을 선언하게 돼서 메모리 초과됨
# sys.setrecursionlimit(10**6) - 재귀깊이를 늘려줘서 런타임에러 방지(pypy3에선 안됨)
# 근데 이 코드를 써줘도 표준 한계치 때문에 stack overflow 돼서 메모리 초과가 난다
# 파이썬은 함수 언어가 아니기 때문에 웬만하믄 반복문으로 가자
'''
import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline

n,r,c=map(int,input().split())
arr=[[0]*(2**n) for _ in range(2**n)]
val=0
def sol(n,x1,y1):
    global val
    if n==1:
        arr[y1][x1]=val
        val+=1
        return
    sol(n//2,x1,y1)
    sol(n//2,x1+n//2,y1)
    sol(n//2,x1,y1+n//2)
    sol(n//2,x1+n//2,y1+n//2)


sol(2**n,0,0)

print(arr[r][c])
'''

# 배열을 안쓰고 사분면으로 나눠서 했는데 또 메모리 초과(stack overflow)
# (r,c)의 사분면이 아니면 넘겨야하는데 조건을 나눠놓고 계속 재귀해서 그런듯
'''
import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline

n,r,c=map(int,input().split())

def sol(n,start,end,y,x):
    if y==r and x==c:
        print(start)
        return
    my=(y+n)//2
    mx=(x+n)//2
    mid=n//2
    val=(end-start)//4
    if r<my and c<mx:
        sol(mid,start,start+val,y,x)
    elif r<my and c>=mx:
        sol(mid,start+val,start+val*2,y,x+mid)
    elif r>=my and c<mx:
        sol(mid,start+val*2,start+val*3,y+mid,x)
    else:
        sol(mid,start+val*3,start+val*4,y+mid,x+mid)
        
sol(2**n,0,(2**n)*(2**n),0,0)
'''
