# 원하는 기준으로 정렬하기(람다 사용)
data = [('a', 15), ('b', 12), ('c', 5)]

print(sorted(data, key = lambda d: d[1]))

data.sort(key = lambda d: d[1])

print(data)