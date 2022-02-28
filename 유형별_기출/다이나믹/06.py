# 두 단어 입력받기
before = input()
after = input()

# 다이나믹 프로그래밍을 위한 DP테이블
dp = [[0]*(len(after) + 1) for _ in range(len(before) + 1)]

# DP 테이블 초기 설정
for i in range(len(after) + 1):
  dp[0][i] = i
for i in range(len(before) + 1):
  dp[i][0] = i

# 최소 편집 거리 계산
for i in range(1, len(before) + 1):
  for j in range(1, len(after) + 1):
    # 문자가 같다면, 왼쪽 위에 해당하는 수를 그대로 대입
    if before[i - 1] == after[j - 1]:
      dp[i][j] = dp[i - 1][j - 1]
    # 문자가 다르다면, 3가지 경우 중에서 최솟값 찾기
    else:
      dp[i][j] = 1 + min(dp[i - 1][j - 1], dp[i][j - 1], dp[i - 1][j])

# 정답 출력
print(dp[-1][-1])