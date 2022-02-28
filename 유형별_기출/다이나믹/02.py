# 삼각형 크기 및 배열 입력받기
size = int(input())
tri = []
for _ in range(size):
  tri.append(list(map(int, input().split())))

for layer in range(1, size):
  for dot in range(len(tri[layer])):
    # 왼쪽 위에서 가져온 경우
    left_up = tri[layer - 1][dot - 1] if dot != 0 else 0
    # 오른쪽 위에서 가져온 경우
    right_up = tri[layer - 1][dot] if dot != len(tri[layer]) - 1 else 0
    # 누적으로 합하기
    tri[layer][dot] += max(left_up, right_up)

# 정답 출력
print(max(tri[-1]))