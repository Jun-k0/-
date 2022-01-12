import heapq

INF = int(1e9)

v, e = map(int,input().split())
start = int(input())

graph = [[] * (v+1)  for _ in range(v+1)]
distance = [INF] * (v+1)

for _ in range(e):
  a, b, c = map(int,input().split())
  graph[a].append((c, b))

def dijkstra(start):
  q = []
  distance[start] = 0
  
  heapq.heappush(q, (0, start))
  while q:
    now = heapq.heappop(q)
    nowDist, nowLoca = now[0], now[1]
    
    for node in graph[nowLoca]:
      nextDist, nextLoca = node[0], node[1]
      
      if distance[nextLoca] > nowDist + nextDist:
        distance[nextLoca] = nowDist + nextDist
        heapq.heappush(q, (nowDist + nextDist ,nextLoca))

dijkstra(start) 
for i in range(1, v+1):
  if distance[i] == INF:
    print("INF")
  else:
    print(distance[i])
