# 입력 회수가 크므로 readline()사용
import sys
input = sys.stdin.readline

# 집의 개수와 길의 개수 입력받기
n, m = map(int, input().split())

# 총 부담할 길의 비용, 길의 개수
result = 0
count = 0

# 부모 확인
def find_parent(parent, x):
  if parent[x] != x:
    parent[x] = find_parent(parent, parent[x])
  return parent[x]

# 합칩합 연산
def union_parent(parent, a, b):
  a = find_parent(parent, a)
  b = find_parent(parent, b)
  if a < b:
    parent[b] = a
  else:
    parent[a] = b

# 부모 리스트 생성 및 초기화
parent = [0]*(n + 1)
for i in range(1, n + 1):
  parent[i] = i

# 크루스칼 알고리즘 사용
roads = []
for _ in range(m):
  a, b, cost = map(int, input().split())
  roads.append((cost, a, b))
roads.sort()

for r in roads:
  # 마을이 2개로 분리되어야 하니까 길은 n - 2 개 있으면 됨
  if count == n - 2:
    break
  cost, a, b = r
  if find_parent(parent, a) != find_parent(parent, b):
    union_parent(parent, a, b)
    result += cost
    count += 1

# 정답 출력
print(result)