# 삼각형 회전하기

# 삼각형 출력함수
def print_triangle(triangle):
  for layer in triangle:
    for i in range(len(layer)):
      print(layer[i], end=' ')
    print()

# 삼각형 우측으로 회전
def rotation_triangle_right(triangle):
  rotated = []
  max_len = len(triangle[-1])
  for i in range(max_len - 1, -1, -2):
    rotated_layer = []
    for layer in triangle:
      if i + 1 < len(layer):
        rotated_layer.append(layer[i + 1])
      if i < len(layer):
        rotated_layer.append(layer[i])
    rotated.append(rotated_layer)
  return rotated

# 삼각형 좌측으로 회전
def rotation_triangle_left(triangle):
  roated_triangle = rotation_triangle_right(triangle)
  return rotation_triangle_right(roated_triangle)

# 테스팅
triangle = [[1], [2, 3, 4], [5, 6, 7, 8, 9], [10, 11, 12, 13, 14, 15, 16]]
print_triangle(triangle)
print('-----------------------------')
triangle_right = rotation_triangle_right(triangle)
print_triangle(triangle_right)
print('-----------------------------')
triangle_left = rotation_triangle_left(triangle)
print_triangle(triangle_left)