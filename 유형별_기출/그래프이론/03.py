import sys
input = sys.stdin.readline

# 집 수와 도로의 수 입력받기
n, m = map(int, input().split())

# 루트 노드 확인
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

# 부모 테이블
parent = [0]*n
for i in range(n):
  parent[i] = i

# 총 비용
result = 0
  
# kruskal
roads = []
for _ in range(m):
  a, b, cost = map(int, input().split())
  result += cost
  roads.append((cost, a, b))
roads.sort()

road_count = 0
for road in roads:
  if road_count >= n - 1:
    break
  cost, a, b = road
  if find_parent(parent, a) != find_parent(parent, b):
    union_parent(parent, a, b)
    result -= cost
    road_count += 1

# 결과 출력
print(result)