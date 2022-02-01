# 조합 사용을 위한 라이브러리
import itertools as it

# 입력 받기
n = int(input())
coin = list(map(int, input().split()))

# 리스트 정렬
coin.sort()

# 1원부터 리스트를 슬라이싱하여 조합으로 확인
answer = 1
while True:
  # 만들 수 있는 금액인지 체크할 플래그
  flag = True

  # 금액보다 작은 만큼만 슬리이싱
  if coin[-1] < answer:
    sliced = coin[:]
  else:
    for i in range(len(coin)):
      if coin[i] > answer:
        sliced = coin[:i]
        break
  
  # 1부터 슬라이싱 리스트 길이까지 조합
  for i in range(1, len(sliced) + 1):
    combi = list(it.combinations(sliced, i))

    price = []
    for c in combi:
      price.append(sum(c))

    if answer in price:
      answer += 1
      flag = False
      break
  
  # 플래그를 통해 확인
  if flag:
    print(answer)
    break


# 훨씬 짧은 코드로 변환 가능 -> 그리디 문제풀이 경험 부족
######################################################


n = input()
data = list(map(int, input().split()))
data.sort()

target = 1
for x in data:
  # 만들 수 없는 금액을 찾았을 때 반복 종료
  if x > target:
    break
  target += x

# 만들 수 없는 금액 출력
print(target)
