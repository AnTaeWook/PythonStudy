from tkinter import E


def solution(n, build_frame):
    
    # 답으로 제출할 건축물들 상태 배열
    status = []
    
    # 빌드 프레임을 순회하며 하나씩 건설 혹은 무시
    for [x, y, build, e] in build_frame:
        flag = 0
        
        # 건축물이 '기둥'일 경우 
        if build == 0:
            # 설치일 경우
            if e == 1:
                # 설치할 수 있는 조건
                if y == 0 or ([x, y - 1, 0] in status) or ([x - 1, y, 1] in status) or ([x, y, 1] in status):
                    status.append([x, y, 0])
            # 삭제일 경우
            else:
                # 기둥 위에 기둥이나 보가 있을 경우
                if ([x, y + 1, 0] in status) or ([x, y + 1, 1] in status) or ([x - 1, y + 1, 1] in status):
                    if ([x, y + 1, 1] in status) or ([x - 1, y + 1, 1] in status):
                        if [x, y + 1, 1] in status:
                            if (([x - 1, y + 1, 1] in status) and ([x + 1, y + 1, 1] in status)) or ([x + 1, y, 0] in status):
                                flag = 1
                            else:
                                continue
                        if [x - 1, y + 1, 1] in status:
                            if (([x - 2, y + 1, 1] in status) and ([x, y + 1, 1] in status)) or ([x - 1, y, 0] in status):
                                flag = 1
                            else:
                                continue
                    if flag:
                        status.remove([x, y, 0])
                else: 
                    status.remove([x, y, 0])
        
        # 건축물이 '보'일 경우
        else:
            
            # 설치일 경우
            if e == 1:
                # 설치할 수 있는 조건
                if (([x - 1, y, 1] in status) and ([x + 1, y, 1] in status)) or ([x, y - 1, 0] in status) or ([x + 1, y - 1, 0] in status):
                    status.append([x, y, 1])
            # 삭제일 경우
            else:
                if ([x, y - 1, 0] not in status) and ([x + 1, y - 1, 0] not in status):
                    if ([x - 1, y - 1, 0] in status) and ([x + 2, y - 1, 0] in status):
                        status.remove([x, y, 1])
                elif ([x, y - 1, 0] in status) and ([x + 1, y - 1, 0] in status):
                    status.remove([x, y, 1])
                else:
                    if [x, y - 1, 0] in status:
                        if [x + 1, y, 1] in status:
                            if [x + 2, y - 1, 0] in status:
                                status.remove([x, y, 1])
                            continue
                        if [x + 1, y, 0] not in status:
                            status.remove([x, y, 1])
                    else:
                        if [x - 1, y, 1] in status:
                            if [x - 1, y - 1, 0] in status:
                                status.remove([x, y, 1])
                            continue
                        if [x, y, 0] not in status:
                            status.remove([x, y, 1])
                        
    status.sort(key=lambda x:(x[0], x[1], x[2]))
    return status


# 풀이 과정은 유사하지만 코드가 월등히 짧게 정답을 작성할 수 있었음(넣으면서 안되는 조건을 찾는게 아닌 넣어놓고 존재할 수있는가 를 판단)
####################################################################################################

# 현재 설치된 구조물이 '가능한' 구조물인지 확인하는 함수
def possible(answer):
    for x, y, stuff in answer:
        if stuff == 0: # 설치된 것이 '기둥'인 경우
            # '바닥 위' 혹은 '보의 한쪽 끝부분 위' 혹은 '다른 기둥 위'라면 정상
            if y == 0 or [x - 1, y, 1] in answer or [x, y, 1] in answer or [x, y - 1, 0] in answer:
                continue
            else:
                return False # 아니라면 거짓(존재할 수없음) 반환
            
        elif stuff == 1: # 설치된 것이 '보'인 경우
            # '한쪽 끝부분이 기둥 위' 혹은 '양쪽 끝부분이 다른 보와 동시에 연결'이라면 정상
            if [x, y - 1, 0] in answer or [x + 1, y - 1, 0] in answer or ([x - 1, y, 1] in answer and [x + 1, y, 1] in answer):
                continue
            else:
                return False # 아니라면 거짓(존재할 수없음) 반환
    
    return True # 존재할 수 있는 구조물임

def solution(n, build_frame):
    answer = []
    for frame in build_frame: # 작업(frame)의 개수는 최대 1,000개
        x, y, stuff, operate = frame
        if operate == 0: # 삭제하는 경우
            answer.remove([x, y, stuff]) # 일단 삭제를 해본 뒤에
            if not possible(answer): # 가능한 구조물인지 확인
                answer.append([x, y, stuff]) # 가능한 구조물이 아니라면 다시 설치
        if operate == 1: # 설치하는 경우
            answer.append([x, y, stuff])
            if not possible(answer): # 가능한 구조물인지 확인
                answer.remove([x, y, stuff]) # 가능한 구조물이 아니라면 다시 삭제
    return sorted(answer) # 정렬된 결과를 반환