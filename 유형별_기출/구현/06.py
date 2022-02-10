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


#
####################################################################################################
