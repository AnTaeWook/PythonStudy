# 입력 받기
n, k = map(int, input().split())
examiner = []
for _ in range(n):
  examiner.append(list(map(int, input().split())))
s, x, y = map(int, input().split())
x, y = x - 1, y - 1 

# 바이러스 위치정보 리스트
virus = []

for i in range(n):
  for j in range(n):
    if examiner[i][j] != 0:
      virus.append([examiner[i][j], i, j])

# 답을 구하려는 위치로부터 가장 가까운 바이러스 찾기
dis = 400
vir = 1000
for v in virus:
  d = abs(x - v[1]) + abs(y - v[2])
  if d < dis:
    dis, vir = d, v[0]
  elif d == dis:
    if v[0] < vir:
      dis, vir = d, v[0]

# 시간과 가장 가까운 거리를 비교해 정답 출력
if dis <= s:
  print(vir)
else:
  print(0)