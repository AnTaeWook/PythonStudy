# 리스트 내 특정 원소 모두 제거하기
# remove()로는 하나밖에 못함

list_old = [1, 2, 2, 3, 4, 5, 5, 6, 7, 8, 8, 8, 9]
remove_set = [2, 5, 8]

list_new = [i for i in list_old if i not in remove_set]

print(list_new)