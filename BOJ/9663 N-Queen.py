import sys

input=sys.stdin.readline

n=int(input())
arr=[[0]*(n) for _ in range(n)]
ans=[]
res=0

def chk(col,cnt):
    for j in range(len(ans)):
        if col in ans or abs(j-cnt)==abs(col-ans[j]):
            return False
    return True
            

def nqueen(cnt):
    global res
    if cnt==n:
        # print(ans)
        res+=1
    else:
        for i in range(n):
            if cnt==0:
                ans.append(int(i))
                nqueen(cnt+1)
                ans.pop()
            else:
                if chk(i,cnt):
                    ans.append(int(i))
                    nqueen(cnt+1)
                    ans.pop()

nqueen(0)
print(res)

'''
한 줄에 하나씩만 넣는 걸 가정하고, row와 col중 하나만 보관하여
반복문을 많이 줄일 수 있었따.
좌표 문제에서 확인
'''
