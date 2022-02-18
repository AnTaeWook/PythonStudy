# 입력 받기
n, l, r = map(int, input().split())
world = []
for _ in range(n):
  world.append(list(map(int, input().split())))

# 일 수
day = 0

# 각 나라 간의 연합 여부 검사함수
def check(unions, x, y):
  dx = [1, 0]
  dy = [0, 1]
  for i in range(len(dx)):
    tx = x
    ty = y

    tx += dx[i]
    ty += dy[i]
    if tx < 0 or tx >= n or ty < 0 or ty >= n:
      continue
    
    # 두 나라가 유니온에 속해있는지 아닌지 검사
    u1 = 1e9
    u2 = 1e9
    if l <= abs(world[x][y] - world[tx][ty]) <= r:
      for i in range(len(unions)):
        if [x, y] in unions[i]:
          u1 = i
        if [tx, ty] in unions[i]:
          u2 = i
      # 하나만 속해 있는 경우
      if u1 != 1e9 and u2 == 1e9:
        unions[u1].append([tx, ty])
      elif u1 == 1e9 and u2 != 1e9:
        unions[u2].append([x, y])
      # 둘 다 연합에 없는 경우
      elif u1 == 1e9 and u2 == 1e9:
        unions.append([[x, y], [tx, ty]])
      # 둘이 같은 엽합에 속해 있는 경우
      elif u1 == u2:
        continue
      # 둘이 다른 연합에 속해 있는 경우
      else:
        unions[u1] += unions[u2]
        del unions[u2]

while True:
  # 연합 리스트
  unions = []

  # 연합 확인
  for x in range(n):
    for y in range(n):
      check(unions, x, y)
  
  # 연합이 없는지 검사
  if len(unions) == 0:
    print(day)
    break

  # 연합 간 인구 이동
  for union in unions:
    sum = 0
    for country in union:
      sum += world[country[0]][country[1]]
    for country in union:
      world[country[0]][country[1]] = sum//len(union)
  
  # 날짜 경과
  day += 1

# 국가들의 연합관계를 파악할 때 이차원 배열로 구현하여 풀었는데,
# BFS를 이용하여 풀 수도 있음