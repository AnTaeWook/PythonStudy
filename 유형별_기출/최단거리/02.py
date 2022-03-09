# 학생 수 와 성적 비교 횟수 입력받기
n, m = map(int, input().split())

# 연결관계 파악을 위한 그래프
graph = [[0]*(n + 1) for _ in range(n + 1)]

# 단방향 연결 입력받으며 대입
for _ in range(m):
  a, b = map(int, input().split())
  graph[a][b] = 1

# 플로이드 워셜 알고리즘을 통한 연결관계 파악
for k in range(1, n + 1):
  for i in range(1, n + 1):
    for j in range(1, n + 1):
      if not graph[i][j] and graph[i][k] and graph[k][j]:
        graph[i][j] = 1
    
# 학생 별 성적을 파악할 수 있는지 조사
count = 0
for s in range(1, n + 1):
  l = []
  for i in range(1, n + 1):
    if graph[s][i]:
      l.append(i)
    if graph[i][s]:
      l.append(i)
  if len(set(l)) == n - 1:
    count += 1

# 정답 출력
print(count)
