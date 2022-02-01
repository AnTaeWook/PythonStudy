# 입력 받기
s = list(map(int, input()))

# 숫자가 하나면 바로 출력
if len(s) <= 1:
  print(s[0])
else:
  # 초기값 설정
  answer = s[0]*s[1] if s[0]*s[1] > s[0] + s[1] else s[0] + s[1]

  # 두 숫자씩 순회하며 값 비교후 답에 더하기
  for i in range(2, len(s)):
    answer = answer*s[i] if answer*s[i] > answer + s[i] else answer + s[i]

  print(answer)


# 시간복잡도는 비슷하지만 더욱 수학적이고 간단한 논리로 접근
############################################################################


data = input()

# 첫 번째 문자를 숫자로 변경하여 대입
result = int(data[0])

for i in range(1, len(data)):
  # 두 수 중에서 하나라도 '0' 혹은 '1'인 경우, 곱하기보다는 더하기 수행
  num = int(data[i])
  if num <= 1 or result <= 1:
    result += num
  else:
    result *= num

print(result)