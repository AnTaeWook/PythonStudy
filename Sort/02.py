# 입력받기
n = int(input())
l = []
for _ in range(n):
  name, score = input().split()
  l.append([name, int(score)])

# 성적에 따라 정렬 후 이름을 출력
for ns in sorted(l, key=lambda x: x[1]):
  print(ns[0], end=' ')
print()