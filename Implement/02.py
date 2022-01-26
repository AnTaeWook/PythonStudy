# implementation - 1번

n = int(input())
count = 0 

for i in range(n + 1):
  for j in range(60):
    for k in range(60):
      h = i
      m = j
      s = k
      # 매 시각 안에 '3'이 포함되어 있다면 카운트 증가
      if '3' in str(h) + str(m) + str(s):
        count += 1

print(count)