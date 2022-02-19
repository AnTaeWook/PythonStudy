# 입력받기
n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# 정렬
a.sort()
b.sort(reverse=True)

# 비교하며 바꿔치기
for i in range(k):
  if a[i] < b[i]:
    a[i], b[i] = b[i], a[i]
  else:
    break

# 정답 출력
print(sum(a))