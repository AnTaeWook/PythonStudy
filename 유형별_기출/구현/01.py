n = list(input())

# 왼쪽 자리수들과 오른쪽 자리수들 리스트 선언
left = list(map(int, n[:len(n)//2]))
right = list(map(int, n[len(n)//2:]))

# 배열끼리의 합이 같으면 LUCKY출력
if sum(left) == sum(right):
  print('LUCKY')
else:
  print('READY')


#
############################################