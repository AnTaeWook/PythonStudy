def add(a, b):
  return a + b

# 일반적인 add 함수
print(add(5, 7))

# lambda로 구현한 add함수
print((lambda a, b: a + b)(5, 7))