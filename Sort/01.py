# 입력받기
n = int(input())
l = []
for _ in range(n):
  l.append(int(input()))

# 정렬 후 출력
for i in sorted(l, reverse=True):
  print(i, end=' ')
print()