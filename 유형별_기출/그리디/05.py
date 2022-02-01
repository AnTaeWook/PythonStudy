# 조합을 사용하기 위한 라이브러리
import itertools as it

# 입력 받기
n, m = map(int, input().split())
bowling = list(map(int, input().split()))

# 조합 생성
combi = list(it.combinations(bowling, 2))

# 조합 중 무게가 같은 조합은 제외하고 카운트
count = 0
for c in combi:
  if c[0] == c[1]:
    continue
  count += 1

# 정답 출력
print(count)


# 조합함수를 쓰지않고 논리적으로 구현 가능 
################################################


n, m = map(int, input().split())
data = list(map(int, input().split()))

# 1부터 10까지의 무게를 담을 수 있는 리스트
array = [0]*11

for x in data:
  # 각 무게에 해당하는 볼링공의 개수 카운트
  array[x] += 1

result = 0
# 1부터 m까지의 각 무게에 대하여 처리
for i in range(1, m + 1):
  # 무게가 i인 볼링공의 개수(A가 선택할 수 있는 개수) 제외
  n -= array[i]
  # B가 선택하는 경우의 수와 곱하기
  result += array[i]*n

print(result)