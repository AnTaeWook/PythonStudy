# 입력 받기
n = int(input())
# dp 테이블 생성
dp = [0]*n
# 첫 못생긴수 = 1
dp[0] = 1

# 2배, 3배, 5배를 위한 인덱스
i2 = i3 = i5 = 0
# 처음에 곱셈값을 초기화
next2, next3, next5 = 2, 3, 5

# 1부터 n까지의 못생긴 수를 찾기
for l in range(1, n):
  # 가능한 곱셈 결과 중에서 가장 작은 수를 선택
  dp[l] = min(next2, next3, next5)
  # 인덱스에 따라서 곱셈 결과를 증가
  if dp[l] == next2:
    i2 += 1
    next2 = dp[i2]*2
  if dp[l] == next3:
    i3 += 1
    next3 = dp[i3]*3
  if dp[l] == next5:
    i5 += 1
    next5 = dp[i5]*5

# n번째 못생긴 수를 출력
print(dp[-1])