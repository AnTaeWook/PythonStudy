# 입력받기
n = int(input())
l = []
for _ in range(n):
  name, kor, eng, math = input().split()
  l.append([name, int(kor), int(eng), int(math)])

# 조건에 맞게 정렬
l.sort(key = lambda x: (-x[1], x[2], -x[3], x[0]))

# 이름만 출력
for i in l:
  print(i[0])

# 정답에서는 입력받을 때 가 아닌 정렬할때 int()함수를 사용했음
# 유의미한 차이 없음