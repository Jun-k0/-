import sys
import heapq
input=sys.stdin.readline

n=int(input())
arr=[]
for _ in range(n):
    a,b=map(int,input().split())
    arr.append([a,b])
arr.sort(key=lambda x:x[0])
q=[]
for i in arr:
    if q:
        minn=heapq.heappop(q)
        if minn<=i[0]:
            heapq.heappush(q,i[1])
        else:
            heapq.heappush(q,minn)
            heapq.heappush(q,i[1])
    else:
        q.append(i[1])

print(len(q))

'''
완전 탐색 시간초과
-> 우선순위 큐 해결 
'''
