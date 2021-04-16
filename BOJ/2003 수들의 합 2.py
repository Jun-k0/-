import sys

input=sys.stdin.readline

n,m=map(int,input().split())
arr=list(map(int,input().split()))

ans,l,r,cnt=0,0,0,0
chk=True

while r<=n-1:
    if(chk):
        cnt+=arr[r]          # 미리 더하지말고 밑에 조건문에서 더했으면 코드가 깔끔해졌을듯
    chk=True
    if cnt==m:
        ans+=1
        r+=1
    else:
        if cnt<m:
            r+=1
        else:
            if l>=r:
                r+=1
            else:
                cnt-=arr[l]
                l+=1
                chk=False
        
print(ans)
'''
투포인터를 써서 완전탐색문제 시간 절약 가능
꼭 정렬된 배열이 아니어도 투포인터를 쓸 수 있었다
근데 음수가 존재하면 쓰면 안될듯.
'''
