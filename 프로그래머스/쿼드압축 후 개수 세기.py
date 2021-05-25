answer=[0]*2
def sol(n,x,y,arr):
    if n==1:
        answer[arr[y][x]]+=1
    else:
        chk=True
        for i in range(y,y+n):
            for j in range(x,x+n):
                if arr[y][x]!=arr[i][j]:
                    chk=False
                    break
        if not chk:
            for i in range(2):
                for j in range(2):
                    sol(n//2,x+i*(n//2),y+j*(n//2),arr)
        else:
            answer[arr[y][x]]+=1

def solution(arr):
    sol(len(arr),0,0,arr)
    return answer
