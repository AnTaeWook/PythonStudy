def solution(N, stages):
    # 스테이지 별 달성한 유저 수 구하기
    reach = [0]*(N + 1)
    for i in stages:
        for j in range(i):
            reach[j] += 1
            
    # 스테이지 별 실패율 구하기
    failer = []
    for i in range(N):
        if reach[i] > 0:
            failer.append([i + 1, stages.count(i + 1)/reach[i]])
        else:
            failer.append([i + 1, 0])
    
    # 문제 조건에 맞게 정렬
    failer.sort(key = lambda x: (-x[1], x[0]))
    
    # 정답에 스테이지 번호만 추가 후 리턴
    answer = []
    for f in failer:
        answer.append(f[0])
    return answer 

# 달성한 유저 수를 구할때 훨씬 간편하고 시간복잡도가 낮게 구하는 법이 있었음

def solution(N, stages):
    answer = []
    length = len(stages)
    
    # 스테이지 번호를 1부터 N까지 증가시키며
    for i in range(1, N + 1):
        # 해당 스테이지에 머물러 있는 사람의 수 계산
        count = stages.count(i)
        
        # 실패율 계산
        if length == 0:
            fail = 0
        else:
            fail = count / length
        
        # 리스트에 (스테이지 번호, 실패율) 원소 삽입
        answer.append((i, fail))
        # 이 부분이 핵심 -> 달성한 사람 구하기
        length -= count
    
    # 실패율을 기준으로 각 스테이지를 내림차순 정렬
    answer.sort(key = lambda x: (-x[1], x[0]))
    
    # 정렬된 스테이지 번호 출력
    answer = [i[0] for i in answer]
    return answer