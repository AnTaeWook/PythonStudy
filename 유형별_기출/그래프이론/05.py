import sys
from collections import deque
input = sys.stdin.readline

# 정답 리스트
answers = []

# 테스트 케이스 만큼 반복
for _ in range(int(input())):
  # 팀 수
  n = int(input())
  # 기존 순위
  rank = list(map(int, input().split()))

  # 기존 순위를 기반으로 그래프 생성
  graph = [[] for _ in range(n + 1)]
  for i in range(1, n + 1):
    graph[rank[i - 1]] = rank[i:]

  # 순위에 따른 우선도 리스트
  indegree = [0]*(n + 1)
  for i in range(1, n + 1):
    indegree[rank[i - 1]] = i - 1

  # 순위 변경 수
  m = int(input())
  # 순위 변경 정보에 따른 그래프와 우선도 변경
  for _ in range(m):
    a, b = map(int, input().split())
    if b in graph[a]:
      graph[a].remove(b)
      graph[b].append(a)
      indegree[a] += 1
      indegree[b] -= 1
    else:
      graph[b].remove(a)
      graph[a].append(b)
      indegree[b] += 1
      indegree[a] -= 1

  # 위상 정렬
  q = deque()
  for i in range(1, n + 1):
    if indegree[i] <= 0:
      q.append(i)
  flag = True
  temp = []
  for _ in range(n):
    if len(q) <= 0:
      answers.append([])
      flag = False
      break
    elif len(q) > 1:
      answers.append([1])
      flag = False
      break
    now = q.popleft()
    temp.append(now)
    for i in graph[now]:
      indegree[i] -= 1
      if indegree[i] <= 0:
        q.append(i)
  if flag:
    answers.append(temp)

# 테스트 케이스 별 정답 출력
for answer in answers:
  if len(answer) <= 0:
    print('IMPOSSIBLE')
  elif len(answer) == 1:
    print('?')
  else:
    for i in answer:
      print(i, end=' ')
    print()