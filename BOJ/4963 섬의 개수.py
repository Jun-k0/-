from collections import deque

# 상하좌우 + 대각선
dx = [1, 0, -1, 0, 1, -1, -1, 1]
dy = [0, 1, 0, -1, 1, 1, -1, -1]

def bfs(x, y, visit, w, h, myMap, q):
  visit[y][x] = True
  q.append((x, y))
  while q:
    now = q.popleft()
    for i in range(8):
      nx = now[0] + dx[i]
      ny = now[1] + dy[i]
      if nx >= 0 and ny >= 0 and nx < w and ny < h:
        if not visit[ny][nx] and myMap[ny][nx] == 1:
          visit[ny][nx] = True
          q.append((nx, ny))

while True:
  w, h = map(int,input().split())
  if w == 0 and h == 0:
    break

  myMap = []
  for _ in range(h):
    myMap.append(list(map(int,input().split())))

  cnt = 0
  visit = [[False] * w for _ in range(h)]
  q = deque()
  for i in range(h):
    for j in range(w):
      if not visit[i][j] and myMap[i][j] == 1:
        bfs(j, i, visit, w, h, myMap, q)
        cnt += 1
  print(cnt)
