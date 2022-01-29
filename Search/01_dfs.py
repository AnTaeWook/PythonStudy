# dfs, bfs - 1번
# dfs풀이

n, m = map(int, input().split())

# 입력받기
arr = []
for _ in range(n):
  arr.append(list(map(int, input())))



# DFS로 특정한 노드를 방문한 뒤에 연결된 모든 노드들도 방문
def dfs(x, y):
  # 주어진 범위를 벗어나는 경우에는 즉시 종료
  if x < 0 or x >= n or y < 0 or y >= m:
    return False
  # 현재 노드를 아직 방문하지 않았다면
  if arr[x][y] == 0:
    # 해당 노드 방문 처리
    arr[x][y] = 1
    # 상, 하, 좌, 우의 위치도 모두 재귀적으로 호출
    dfs(x - 1, y)
    dfs(x, y - 1)
    dfs(x + 1, y)
    dfs(x, y + 1)
    return True
  return False


# 배열을 순회하며 dfs수행 및 카운트
count = 0
for i in range(n):
  for j in range(m):
    # 현재 위치에서 DFS 수행
    if dfs(i, j):
      count += 1

print(count)