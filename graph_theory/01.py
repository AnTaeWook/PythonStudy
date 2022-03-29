# 팀 확인하기
def find_parent(parent, x):
  if parent[x] != x:
    parent[x] = find_parent(parent, parent[x])
  return parent[x]

# 팀 합치기
def union_parent(parent, a, b):
  a = find_parent(parent, a)
  b = find_parent(parent, b)
  if a < b:
    parent[b] = a
  else:
    parent[a] = b

# 번호와 연산 횟수 입력받기
n, m = map(int, input().split())

# 부모 리스트 생성 및 초기화
parent = [0] * (n + 1)
for i in range(n + 1):
  parent[i] = i

# 출력결과를 저장할 리스트
answer = []
  
# 연산 입력받기
for _ in range(m):
  t, a, b = map(int, input().split())
  # 팀 합치기
  if t == 0:
    union_parent(parent, a, b)
  # 같은 팀 여부 확인
  else:
    if find_parent(parent, a) == find_parent(parent, b):
      answer.append('YES')
    else:
      answer.append('NO')

# 정답 출력
for a in answer:
  print(a)