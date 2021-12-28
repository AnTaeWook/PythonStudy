import copy

l1 = [1, 2, 3, 4]
#깊은 복사
l2 = copy.deepcopy(l1)

print(l2)
l2[1] = 10
print(l1)