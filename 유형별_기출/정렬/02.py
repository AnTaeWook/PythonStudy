# 입력 받기
n = int(input())
house = list(map(int, input().split()))

# 집 위치 정렬
house.sort()

# 집 개수가 홀수인 경우
if len(house)%2 == 1:
  print(house[len(house)//2])
# 짝수인 경우
else:
  # 중앙 두 집만 비교
  dis1, dis2 = 0, 0
  for i in range(len(house)):
    if i == len(house)//2:
      continue
    dis1 += abs(house[i] - house[len(house)//2])
  for i in range(len(house)):
    if i == len(house)//2 - 1:
      continue
    dis1 += abs(house[i] - house[len(house)//2 - 1])
  if dis2 <= dis1:
    print(house[len(house)//2 - 1])
  else:
    print(house[len(house)//2])
  
# 논리적으로 생각하면 집의 개수가 짝수인 경우에도 가운데 두 집 모두
# 최소거리가 같기 때문에 왼쪽집이 항상 답임

n = int(input())
data = list(map(int, input().split()))
data.sort()

# 중간값(median)을 출력
print(data[(n - 1)//2])
