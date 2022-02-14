from collections import deque

n, m, k, x = map(int, input().split())

# 방문여부, 거리, 마을지도
town = [[] for _ in range(n + 1)]
visited = [False]*(n + 1)
distance = [0]*(n + 1)

# 도로 반영
for _ in range(m):
  start, end = map(int, input().split())
  town[start].append(end)

# 정답을 담을 배열
answer = []

# bfs
queue = deque([x])
visited[x] = True

while queue:
  break_flag = 0
  t = queue.popleft()
  for nt in town[t]:
    # 방문 안했다면
    if not visited[nt]:
      # 거리 설정
      distance[nt] = distance[t] + 1
      visited[nt] = True
      queue.append(nt)
      # 정답에 해당하는 거리면
      if distance[nt] == k:
        answer.append(nt)
      # 정답을 초가하였다면
      elif distance[nt] > k:
        break_flag = 1
        break
  if break_flag:
    break

# 정답이 없는지 검사
if len(answer) <= 0:
  print(-1)

# 정답 출력
answer.sort()
for a in answer:
  print(a)


#
#########################################