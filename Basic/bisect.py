# 이진 탐색트리

# bisect 라이브러리 사용
import bisect as bs

a = [1, 2, 3, 4, 4, 4, 5, 6]
x = 4

# 정렬 순서를 유지하며 삽입할 가장 왼쪽 혹은 오른쪽 인덱스를 찾는 메서드
print(bs.bisect_left(a, x))
print(bs.bisect_right(a, x))

# 위 메서드를 이용하여 정렬된 데이터에서 특정 범위에 속하는 원소 개수를 구할 수 있다
def count_range(a, left_value, right_value):
  l = bs.bisect_left(a, left_value)
  r = bs.bisect_right(a, right_value)
  return r - l

print(count_range(a, 2, 5))
print(count_range(a, -144, 455))