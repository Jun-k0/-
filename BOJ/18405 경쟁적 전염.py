import heapq

dx = [1, 0 ,-1, 0]
dy = [0, 1, 0 ,-1]

n, k = map(int, input().split())
graph = []
q = []

for _ in range(n):
  graph.append(list(map(int, input().split())))

# 행과 열 순서 주의!
s, y, x = map(int, input().split())

def BFS():
  while q:
    nowTime, val, nowX, nowY = heapq.heappop(q)
    for i in range(4):
      nextX = nowX + dx[i]
      nextY = nowY + dy[i]
      if nextX >= 0 and nextY >= 0 and nextX < n and nextY < n:
        if graph[nextY][nextX] == 0 and nowTime < s:
          heapq.heappush(q, (nowTime + 1, val, nextX, nextY))
          graph[nextY][nextX] = val
      

for i in range(n):
  for j in range(n):
    if graph[i][j] != 0:
      heapq.heappush(q, (0, graph[i][j], j, i))

BFS()

# 행과 열 순서 주의!
print(graph[y-1][x-1])
