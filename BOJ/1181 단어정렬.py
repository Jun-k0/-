import sys

input=sys.stdin.readline

n=int(input().rstrip())
arr=[]
for _ in range(n):
    st=input().rstrip()
    if st not in arr:
        arr.append(st)
arr.sort(key=lambda x:(len(x),x)) # 정렬하는 우선순위 정함

for i in arr:
    print(i)

