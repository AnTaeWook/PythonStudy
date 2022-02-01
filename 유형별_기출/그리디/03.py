# 입력 받기
s = list(map(int, input()))

# 숫자가 몇 번 바뀌는지 확인
change = 0
for i in range(len(s) - 1):
  if s[i] != s[i + 1]:
    change += 1

# 정답 출력
print((change + 1)//2)


# 더 이해하기 쉽고 직관적이지만 코드가 길어짐
###############################


data = input()
# 전부 0으로 바꾸는 경우
count0 = 0 
# 전부 1로 바꾸는 경우
count1 = 0

# 첫 번째 원소에 대해서 처리
if data[0] == '1':
  count0 += 1
else:
  count1 += 1

# 두 번째 원소부터 모든 원소를 확인하며
for i in range(len(data) - 1):
  if data[i] != data[i + 1]:
    # 다음 수에서 1로 바뀌는 경우
    if data[i + 1] == '1':
      count0 += 1
    # 다음 수에서 0으로 바뀌는 경우
    else:
      count1 += 1

print(min(count0, count1))