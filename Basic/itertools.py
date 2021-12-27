# itertools 라이브러리 사용
import itertools as it

data = ['A', 'B', 'C']

# 순열
print(list(it.permutations(data, 2)))

# 조합
print(list(it.combinations(data, 2)))

# 순열_중복허용
print(list(it.product(data, repeat = 2)))

# 조합_중복허용
print(list(it.combinations_with_replacement(data, 2)))