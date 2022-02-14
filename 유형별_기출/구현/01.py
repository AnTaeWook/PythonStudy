n = list(input())

# 왼쪽 자리수들과 오른쪽 자리수들 리스트 선언
left = list(map(int, n[:len(n)//2]))
right = list(map(int, n[len(n)//2:]))

# 배열끼리의 합이 같으면 LUCKY출력
if sum(left) == sum(right):
  print('LUCKY')
else:
  print('READY')


# 답이랑 크게 방향이 다르지 않음 슬라이싱과 인덱싱 차이
############################################

n = input()
length = len(n)
summary = 0

# 왼쪽 부분의 자릿수 합 더하기
for i in range(length // 2):
  summary += int(n[i])
  
# 오른쪽 부분의 자릿수 합 빼기
for i in range(length // 2, length):
  summary -= int(n[i])

# 왼쪽 부분과 오른쪽 부분의 자릿수 합이 동일한지 검사
if summary == 0:
  print('LUCKY')
else:
  print('READY')
