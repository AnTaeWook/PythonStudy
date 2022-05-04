import sys
import heapq
input = sys.stdin.readline
INF = float('inf')

# 다익스트라 알고리즘
def dijkstra(start, distance, graph):
  distance[start] = 0
  q = []
  heapq.heappush(q, [0, start])
  while q:
    d, v = heapq.heappop(q)
    if distance[v] < d:
      continue
    for ver, dis in graph[v]:
      cost = dis + distance[v]
      if cost < distance[ver]:
        distance[ver] = cost
        heapq.heappush(q, [cost, ver])

# 입력값 받기
N, M, X = map(int, input().split())

# 다익스트라 알고리즘 사용을 위한 그래프(정방향, 역방향)
graphFrom = [[] for _ in range(N + 1)]
graphTo = [[] for _ in range(N + 1)]

# 간선 입력 받기
for _ in range(M):
  a, b, c = map(int, input().split())
  graphFrom[a].append([b, c])
  graphTo[b].append([a, c])  

# 파티에서 부터의 최단거리
distanceFrom = [INF]*(N + 1)
dijkstra(X, distanceFrom, graphFrom)

# 파티까지의 최단거리
distanceTo = [INF]*(N + 1)
dijkstra(X, distanceTo, graphTo)

# 왕복 최장거리 구하기
maximum = -INF
for i in range(1, N + 1):
  maximum = max(maximum, distanceFrom[i] + distanceTo[i])

print(maximum)
