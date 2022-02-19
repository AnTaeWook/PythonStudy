import heapq
import sys

# 입력받기
n = int(input())
cards = []
for _ in range(n):
  heapq.heappush(cards, int(sys.stdin.readline()))

# 총 비교횟수
comparison = 0

# 카드덱 개수가 1개면 비교 불필요
if len(cards) <= 1:
  print(0)
else:
  # 가장 적은 수의 덱 2개를 더해서 비교횟수에 누적한 후
  # 더한 수를 다시 카드 목록에 추가
  while len(cards) >= 2:
    c1 = heapq.heappop(cards)
    c2 = heapq.heappop(cards)
    comparison += c1 + c2
    heapq.heappush(cards, c1 + c2)
  print(comparison)
  
# heapq 사용법 익숙해지기(매우 중요)