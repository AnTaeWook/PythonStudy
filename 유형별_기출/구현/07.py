import itertools
import copy

# 치킨집 위치와 거리를 구하는 함수
def chicken(town, y, x, store):
  # 집과의 거리
  dis = 1

  while True:
    for s in store:
      if abs(s[0] - y) + abs(s[1] - x) == dis:
        return dis
    dis += 1

n, m = map(int, input().split())
# 마을 상태
town = []
# 치킨집 위치
store = []
for _ in range(n):
  town.append(list(map(int, input().split())))

# 치킨집 위치부터 저장
for y in range(n):
  for x in range(n):
    if town[y][x] == 2:
      store.append([y, x])

# 남겨야하는 치킨집 개수만큼 조합생성
lefted = list(itertools.combinations(store, m))

chicken_distance = []

# 치킨집이 남겨지는 상황 순회
for situation in lefted:
  # 상황마다 치킨거리 구하기
  cd = 0
  for y in range(n):
    for x in range(n):
      if town[y][x] == 1:
        cd += chicken(town, y, x, situation)
  chicken_distance.append(cd)

# 도시의 치킨 거리의 최소값 출력
print(min(chicken_distance))

# 풀이는 유사하나 집을 탐색하며 찾지말고 튜플의 배열로 저장해서 꺼내쓰는게 시간복잡도를 줄이는 방법임 
################################################################################################