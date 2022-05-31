import string

# 10진수의 값을 n진수로 변환하는 함수
tmp = string.digits+string.ascii_lowercase
def convert(num, base) :
    q, r = divmod(num, base)
    if q == 0 :
        return tmp[r] 
    else :
        return convert(q, base) + tmp[r]

print(convert(10,2))
print(convert(10,3))
print(convert(10,4))
print(convert(10,5))