from collections import deque
import copy

# 강의 개수 입력받기
n = int(input())

# 해당 강의를 듣기 위해 필요한 시간
required_time = [0]*(n + 1)

# 선수 과목 개수 리스트
indegree = [0]*(n + 1)

# 강의들의 선수 관계를 파악하기 위한 그래프
graph = [[] for _ in range(n + 1)]

# 선수 관계와 시간을 입력받기
for i in range(1, n + 1):
  data = list(map(int, input().split()))
  required_time[i] = data[0]
  # 선수 과목 리스트
  preReq = data[1:-1]
  for p in preReq:
    graph[p].append(i)
  indegree[i] = len(preReq)
    
# 위상 정렬 알고리즘
q = deque()
# 각 과목을 수강하는데 걸리는 총 시간(DP 테이블)
result = copy.deepcopy(required_time)
for i in range(1, n + 1):
  if indegree[i] <= 0:
    q.append(i)

while q:
  now = q.popleft()
  for i in graph[now]:
    result[i] = max(result[i], result[now] + required_time[i])
    indegree[i] -= 1
    if indegree[i] <= 0:
      q.append(i)

# 정답 출력
result = result[1:]
for r in result:
  print(r)