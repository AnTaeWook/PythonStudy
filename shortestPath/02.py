import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

# 도시 수, 간선, 시작 도시 수 입력받기
n, m, s = map(int, input().split())

# 도시 그래프, 최단거리 리스트 초기화
graph = [[] for _ in range(n + 1)]
distance = [INF]*(n + 1)

# 간선정보 입력받기
for _ in range(m):
  a, b, c = map(int, input().split())
  graph[a].append((b, c))

# 다익스트라 알고리즘
def dijkstra(start):
  distance[start] = 0
  q = []
  heapq.heappush(q, (0, start))
  # 우선순위 큐 이용
  while q:
    dist, now = heapq.heappop(q)
    if distance[now] < dist:
      continue

    for i in graph[now]:
      cost = dist + i[1]
      if cost < distance[i[0]]:
        distance[i[0]] = cost
        heapq.heappush(q, (cost, i[0]))

# 다익스트라 수행
dijkstra(s)

# 정답 계산
recv = n - distance.count(INF)
max_time = -1
for d in distance:
  if d > max_time and d < INF:
    max_time = d

# 정답 출력
print(recv, max_time)