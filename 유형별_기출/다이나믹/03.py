# 입력 받기
n = int(input())
task = []
for _ in range(n):
  task.append(list(map(int, input().split())))

# 최대 이윤
max_money = 0
# dp 테이블
dp = [0]*(n + 1)

# 다이나믹 프로그래밍 시작
for i in range(n - 1, -1, -1):
  if task[i][0] + i <= n:
    dp[i] = max(task[i][1] + dp[i + task[i][0]], max_money)
    max_money = dp[i]
  else:
    dp[i] = max_money

# 최대 이윤 출력
print(max_money)