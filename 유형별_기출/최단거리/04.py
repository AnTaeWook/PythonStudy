INF = int(1e9)
import heapq

# 입력 받기
n, m = map(int, input().split())

# 그래프 초기화 및 간선 입력받기
graph = [[] for _ in range(n + 1)]
for _ in range(m):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

# 다익스트라 알고리즘
distance = [INF]*(n + 1)
q = []
s = 1
heapq.heappush(q, [0, s])
while q:
  d, v = heapq.heappop(q)
  if distance[v] < d:
    continue
  distance[v] = d
  for i in graph[v]:
    if d + 1 < distance[i]:
      heapq.heappush(q, [d + 1, i])

# 가장 긴 최단거리 추출
distance = distance[1:]
count = 0
maximum = max(distance)
mv = []
for i in range(len(distance)):
  if distance[i] == maximum:
    mv.append(i + 1)

# 정답 출력
print(mv[0], maximum, len(mv))