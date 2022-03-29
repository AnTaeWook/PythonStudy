# 탑승구 수와 비행기 수 입력받기
g = int(input())
p = int(input())

# 부모 리스트 생성 및 초기화
parent = [0]*(g + 1)
for i in range(1, g + 1):
  parent[i] = i

# 들어오는 비행기 리스트 입력받기
plains = []
for _ in range(p):
  plains.append(int(input()))
  
# 부모 노드 확인하기
def find_parent(parent, x):
  if parent[x] != x:
    parent[x] = find_parent(parent, parent[x])
  return parent[x]

# 들어올 수 있는 비행기 수
count = 0
    
# 들어오는 비행기 마다 가능한 최대 노드로 배정
for plain in plains:
  goto = find_parent(parent, plain)
  # 비행가기 들어올 수 없는 상황
  if goto <= 0:
    break
  parent[goto] = goto - 1
  count += 1

# 정답 출력
print(count)