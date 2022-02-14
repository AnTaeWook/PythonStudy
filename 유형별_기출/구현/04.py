import copy

def rotation(arr):
    temp = copy.deepcopy(arr)
    for i in range(len(arr)):
        for j in range(len(arr)):
            arr[i][j] = temp[len(arr) - j - 1][i]

def solution(key, lock):
    
    # 새 배열 생성
    arr = [[0]*(len(lock) + (2*len(key)) - 2) for _ in range((len(lock) + (2*len(key)) - 2))]
    
    # 새 배열 중앙에 자물쇠 값 대입
    for i in range(len(key) - 1, len(key) + len(lock) - 1):
        for j in range(len(key) - 1, len(key) + len(lock) - 1):
            arr[i][j] = lock[1 - len(key) + i][1 - len(key) + j]
    
    # 키 배열 대입 및 비교
    for _ in range(4):
        
        for x in range(len(lock) + len(key) - 1):
            for y in range(len(lock) + len(key) - 1):
                
                # temp 배열에 원본 배열arr 복사 후 key 대입
                temp = copy.deepcopy(arr)
                for i in range(len(key)):
                    for j in range(len(key)):
                        temp[i + x][j + y] += key[i][j]

                # lock 부분 모두 1인지 검사
                for i in range(len(key) - 1, len(key) + len(lock) - 1):
                    for j in range(len(key) - 1, len(key) + len(lock) - 1):
                        if temp[i][j] != 1:
                            break
                        if i == len(key) + len(lock) - 2 and j == len(key) + len(lock) - 2:
                            return True
                    else:
                        continue
                    break
                    
        # key 배열 회전
        rotation(key)
        
    return False


# 이 문제 또한 완전탐색으로 접근하는것이 맞음
##################################################################################################