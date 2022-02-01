# 솔루션 함수
def solution(food_times, k):
  time = 0
  i = 0

  # food_time 배열을 순회하며 0인 부분은 스킵
  while True:
    # 먹을 음식이 하나도 없는지 검사
    if sum(food_times) == 0:
      return -1

    idx = i % len(food_times)
    # 0인 부분 스킵
    if food_times[idx] <= 0:
      i += 1
      continue

    # 통신량이 발생한 시점에 먹어야 할 음식 번호 리턴
    if time == k:
      return i % len(food_times) + 1

    # 해당 음식 먹음과 동시에 시간 증가
    food_times[idx] -= 1
    i += 1
    time += 1


# 정확도는 맞았지만 효율성에서 떨어짐 -> 효율성 개선 가능
########################################################


import heapq

# 솔루션 함수
def solution(food_times, k):
  # 전체 음식을 먹는 시간보다 k가 크거나 같다면 -1
  if sum(food_times) <= k:
    return -1
  
  # 시간이 적은 음식부터 빼야 하므로 우선순위 큐를 이용
  q = []
  for i in range(len(food_times)):
    # (음식 시간, 음식 번호) 형태로 우선순위 큐에 삽입
    heapq.heappush(q, (food_times[i], i + 1))

  # 먹기 위해 사용한 시간
  sum_value = 0
  # 직전에 다 먹은 음식 시간
  previous = 0
  # 남은 음식의 개수
  length = len(food_times)
  
  # sum_value + (현재의 음식 시간 - 이전 음식 시간) * 현재 음식 개수와 k 비교
  while sum_value + ((q[0][0] - previous)*length) <= k:
    now = heapq.heappop(q)[0]
    sum_value += (now - previous)*length
    # 다 먹은 음식 제외
    length -= 1
    # 이전 음식 시간 재설정  
    previous = now
  
  # 남은 음식 중에서 몇 번째 음식인지 확인하여 출력
  # 음식의 번호 기준으로 정렬
  result = sorted(q, key = lambda x: x[1])
  return result[(k - sum_value)%length][1]

