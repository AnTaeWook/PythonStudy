# heapq 라이브러리 사용
import heapq as hq

def heapsort(iterable):
  h = []
  result = []
  # 모든 원소를 차례대로 힙에 삽입
  for value in iterable:
    hq.heappush(h, value)

  #힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
  for _ in range(len(h)):
    result.append(hq.heappop(h))
  
  return result

result = heapsort([1, 3, 0, 12, 5, 2, 87])
print(result)

"""
파이썬은 기본 min heap이므로 
내림차순의 경우 부호를 바꿔서 넣고 빼는 방법으로 구현 가능!
"""