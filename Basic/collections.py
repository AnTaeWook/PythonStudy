# collections 라이브러리 사용
import collections as ct

"""
왜 deque를 사용하는가? 
-> 가장 앞쪽에 원소를 꺼내거나 추가할 경우 시간복잡도가 O(1)이기 때문(리스트는 O(n))
"""
data = ct.deque([2, 3, 4])
data.appendleft(10)
data.append(20)

print(data)
data = list(data)
print(data)

# list 사용
# l = ['a', 'a', 'b', 'a', 'c', 'd', 'c']

# print(l.count('a'))
# print(l.count('b'))

# counter 사용
c = ct.Counter(['a', 'a', 'b', 'a', 'c', 'd', 'c'])

print(c['a'])
print(c['b'])