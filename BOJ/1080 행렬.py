n, m = map(int, input().split())
beforeMatrix = [[] * m for _ in range(n)]
afterMatrix = [[] * m for _ in range(n)]
ans = 0

def changeMatrix(x, y):
  for i in range(y, y+3):
    for j in range(x, x+3):
      if beforeMatrix[i][j] == 0:
        beforeMatrix[i][j] = 1
      elif beforeMatrix[i][j] == 1:
        beforeMatrix[i][j] = 0

for i in range(n):
  temps = input()
  for temp in temps:
    beforeMatrix[i].append(int(temp))
    
for i in range(n):
  temps = input()
  for temp in temps:
    afterMatrix[i].append(int(temp))

for i in range(n):
  for j in range(m):
    if i <= n-3 and j <= m-3 and beforeMatrix[i][j] != afterMatrix[i][j]:
      changeMatrix(j, i)
      ans += 1

if beforeMatrix != afterMatrix:
  ans = -1

print(ans)
