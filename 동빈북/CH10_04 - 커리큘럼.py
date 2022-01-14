from collections import deque
import copy

n = int(input())
classTime = [-1] * (n + 1)
indegree = [0] * (n + 1)
preClass = [[] for _ in range(n + 1)] 
q = deque()

for i in range(1,n+1):
  arr = list(map(int, input().split()))
  classTime[i] = arr[0]
  j = 1
  
  # for data in arr[1:-1]로 대체 가능하다!
  
  while True:
    if arr[j] == -1:
      break
    preClass[arr[j]].append(i)
    indegree[i] += 1
    j += 1

classTimeCopy = copy.deepcopy(classTime)	# 깊은 복사

for i in range(1, n+1):
  if indegree[i] == 0:
    q.append(i)

while q:
  now = q.popleft()
  for pclass in preClass[now]:
    indegree[pclass] -= 1
    classTime[pclass] = max(classTime[pclass], classTime[now] + classTimeCopy[pclass])
    if indegree[pclass] == 0:
      q.append(pclass)

for time in classTime:
  if time == -1:
    continue
  print(time)
