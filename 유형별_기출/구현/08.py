from itertools import permutations
import copy

def solution(n, weak, dist):
    answer = 10
    
    # 원형을 일자로 핌
    weaks = copy.deepcopy(weak)
    for w in weak:
        weaks.append(w + n)
    
    # 친구들 배치 순열
    dists = list(permutations(dist, len(dist)))
    
    # 각 배치마다 
    for d in dists:
        # 각 시작점 마다
        for i in range(len(weak)):
            # 점검한 친구 수
            count = 1
            # 첫 시작 위치
            position = weaks[i]
            # 각 친구 마다
            for idx in range(len(dist)):
                check = 0
                position += d[idx]
                # 약점을 얼마나 점검했는지 확인
                for j in range(i, len(weak) + i):
                    if position < weaks[j]:
                        position = weaks[j]
                        break
                    check += 1
                # 모든 약점을 점검했는지 확인
                if check >= len(weak):
                    if count < answer:
                        answer = count
                    break
                count += 1
    
    if answer == 10:
        answer = -1
    return answer