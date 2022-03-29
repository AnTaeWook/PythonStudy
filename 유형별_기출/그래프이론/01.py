# 여행지 수와 여행할 도시 수 입력받기
n, m = map(int, input().split())

# 부모 노드 찾기
def find_parent(parent, x):
  if parent[x] != x:
    parent[x] = find_parent(parent, parent[x])
  return parent[x]

# union 합 연산
def union_parent(parent, a, b):
  a = find_parent(parent, a)
  b = find_parent(parent, b)
  if a > b:
    parent[a] = b
  else:
    parent[b] = a

# 부모 노드 리스트 생성 및 초기화
parent = [0]*(n + 1)
for i in range(1 , n + 1):
  parent[i] = i

# 경로에 따라 유니온 연산 수행
for i in range(1, n + 1):
  data = list(map(int, input().split()))
  for j in range(n):
    if data[j] > 0:
      union_parent(parent, i, j + 1)

# 여행이 가능한지 판별하는 플래그
can_travel = True
      
# 여행 계획 입력 받고 검사
travel = list(map(int, input().split()))
for i in range(len(travel) - 1):
  if find_parent(parent, travel[i]) != find_parent(parent, travel[i + 1]):
    can_travel = False
    break

# 정답 출력
if can_travel:
  print('YES')
else:
  print('NO')