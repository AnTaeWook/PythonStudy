# 유클리드 호제법을 이용한 최대공약수 함수
def mygcd(a, b):
  while a!=b:
    if a > b:
      a -= b
    else:
      b -= a
  return a

print(mygcd(5, 15))