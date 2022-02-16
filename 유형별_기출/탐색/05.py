###### 백트래킹 ###### 매우중요 ######

# 입력받기
n = int(input())
numbers = list(map(int, input().split()))
op = list(map(int, input().split()))

maximum = -1e9
minimum = 1e9

def dfs(depth, total, plus, minus, multiple, divide):
  global maximum, minimum
  if depth == n:
    maximum = max(maximum, total)
    minimum = min(minimum, total)
    return

  if plus:
    dfs(depth + 1, total + numbers[depth], plus - 1, minus, multiple, divide)
  if minus:
    dfs(depth + 1, total - numbers[depth], plus, minus - 1, multiple, divide)
  if multiple:
    dfs(depth + 1, total * numbers[depth], plus, minus, multiple - 1, divide)
  if divide:
    dfs(depth + 1, int(total / numbers[depth]), plus, minus, multiple, divide - 1)

dfs(1, numbers[0], op[0], op[1], op[2], op[3])
print(maximum, minimum, sep='\n')

####################################################################################
###### 순열 ######
from itertools import permutations

# 입력받기
n = int(input())
numbers = list(map(int, input().split()))
op = list(map(int, input().split()))
oper = ['+', '-', '*', '/']
operators = []
for i in range(len(op)):
  for _ in range(op[i]):
    operators.append(oper[i])

# 연산 결과값을 담을 배열
result = []

# 연산자를 배치하는 모든 경우의 수
opers = list(permutations(operators, len(operators)))

# 모든 경우를 탐색하며 결과를 결과 배열에 추가
for case in opers:
  r = numbers[0]
  for i in range(len(case)):
    if case[i] == '+':
      r += numbers[i + 1]
    elif case[i] == '-':
      r -= numbers[i + 1]
    elif case[i] == '*':
      r *= numbers[i + 1]
    else:
      r = int(r/numbers[i + 1])
  result.append(r)

# 최대와 최소 출력
result.sort()
print(result[-1])
print(result[0])