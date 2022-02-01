# 입력 받기
n = int(input())
scarity = list(map(int, input().split()))
group = 0

# 1부터 같은 공포도 끼리 최대한 묶기
for i in range(1, n + 1):
  group += scarity.count(i)//i

print(group)


# 문제를 잘못 읽고 풀었음 -> 문제 이해 실패
############################################ 


n = int(input())
data = list(map(int, input().split()))
data.sort()

# 총 그룹의 수
result = 0
# 현재 그룹에 포함된 모험가의 수
count = 0

# 공포도를 낮은 것부터 하나씩 확인하며 모험가를 포함시키기
for i in data:
  count += 1
  if count >= i:
    result += 1
    count = 0

print(result)




