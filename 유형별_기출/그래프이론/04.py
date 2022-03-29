import sys
input = sys.stdin.readline

# 행성 수 입력받기
n = int(input().rstrip())

# 행성들의 좌표와 번호 입력받기
planets = []
for i in range(n):
  x, y, z = map(int, input().split())
  planets.append((i, x, y, z))

# 부모노드 찾기
def find_parent(parent, x):
  if parent[x] != x:
    parent[x] = find_parent(parent, parent[x])
  return parent[x]

# 유니온 연산
def union_parent(parent, a, b):
  a = find_parent(parent, a)
  b = find_parent(parent, b)
  if a < b:
    parent[b] = a
  else:
    parent[a] = b

# 부모리스트 생성 및 초기화
parent = [0]*n
for i in range(n):
  parent[i] = i

# x, y, z 좌표 기준으로 각각 정렬
sort_lists = []
sort_lists.append(sorted(planets, key=lambda x: x[1]))
sort_lists.append(sorted(planets, key=lambda x: x[2]))
sort_lists.append(sorted(planets, key=lambda x: x[3]))

diff_list = []
# 각 좌표 기준 순차적인 좌표 차 계산
for i in range(3):
  for j in range(len(sort_lists[i]) - 1):
    diff_list.append((abs(sort_lists[i][j][i + 1] - sort_lists[i][j + 1][i + 1]),
                          sort_lists[i][j][0], sort_lists[i][j + 1][0]))
# 거리 차 기준으로 정렬
diff_list.sort(key = lambda x: x[0])

# 거리가 제일 가까운 행성부터 kruskal 수행
result = 0
planet_count = 0
for diff in diff_list:
  if planet_count >= n - 1:
    break
  cost, a, b = diff
  if find_parent(parent, a) != find_parent(parent, b):
    union_parent(parent, a, b)
    result += cost
    planet_count += 1

# 정답 출력
print(result)