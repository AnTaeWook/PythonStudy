# 다차원 배열에서 특정 원소 기준으로 정렬할 때

arr = [[1, 10], [3, 8], [2, 9], [4, 7]]
# 첫 번째 원소 기준 오름차순
arr.sort(key=lambda x:x[0])
print(arr)
# 두 번째 원소 기준 오름차순
arr.sort(key=lambda x:x[1])
print(arr)

arr = [[2, 10], [3, 10], [2, 9], [4, 7]]
# 두 번째 원소 기준 오름차순 -> 같으면 첫 번째 원소 기준 오름차순
arr.sort(key=lambda x:(x[1], x[0]))
print(arr)

arr = [[2, 10], [3, 10], [2, 9], [4, 7]]
# 두 번째 원소 기준 오름차순 -> 같으면 첫 번째 원소 기준 내림차순
arr.sort(key=lambda x:(x[1], -x[0]))
print(arr)