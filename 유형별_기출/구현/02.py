s = input()

# 문자들 배열
cl = []
# 숫자들 배열
num = []

# 순회하며 알맞은 배열에 추가
for c in s:
  if 'A' <= c and c <= 'Z':
    cl.append(c)
  else:
    num.append(int(c))

# 알파벳 정렬
cl.sort()

for c in cl:
  print(c, end='')
print(sum(num))


# 정답과 거의 동일 -> 숫자만 문자열로 추가하는게 전부
################################