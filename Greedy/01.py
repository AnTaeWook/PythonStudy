# greedy - 1번

n, m, k = map(int, input().split())
data = list(map(int, input().split()))

# 정렬 후 가장 큰 수, 두 번째로 큰 수 초기화
data.sort(reverse=True)
first = data[0]
second = data[1]

# 가장 큰 수가 더해지는 횟수 계산
count = int(m/(k + 1)) * k
count += m%(k + 1)

result = 0
result += count * first # 가장 큰 수 더하기
result += (m - count) * second # 두 번째로 큰 수 더하기

print(result)
