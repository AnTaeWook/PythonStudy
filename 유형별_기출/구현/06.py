def solution(n, build_frame):
    
    # 답으로 제출할 건축물들 상태 배열
    status = []
    
    # 빌드 프레임을 순회하며 하나씩 건설 혹은 무시
    for build in build_frame:
        flag = 0
        
        # 건축물이 '기둥'일 경우 
        if build[2] == 0:
            # 설치일 경우
            if build[3] == 1:
                # 설치할 수 있는 조건
                if build[1] == 0 or ([build[0], build[1] - 1, 0] in status) or ([build[0] - 1, build[1], 1] in status) or ([build[0], build[1], 1] in status):
                    status.append([build[0], build[1], 0])
            # 삭제일 경우
            else:
                # 기둥 위에 기둥이나 보가 있을 경우
                if ([build[0], build[1] + 1, 0] in status) or ([build[0], build[1] + 1, 1] in status) or ([build[0] - 1, build[1] + 1, 1] in status):
                    if ([build[0], build[1] + 1, 1] in status) or ([build[0] - 1, build[1] + 1, 1] in status):
                        if [build[0], build[1] + 1, 1] in status:
                            if (([build[0] - 1, build[1] + 1, 1] in status) and ([build[0] + 1, build[1] + 1, 1] in status)) or ([build[0] + 1, build[1], 0] in status):
                                flag = 1
                            else:
                                continue
                        if [build[0] - 1, build[1] + 1, 1] in status:
                            if (([build[0] - 2, build[1] + 1, 1] in status) and ([build[0], build[1] + 1, 1] in status)) or ([build[0] - 1, build[1], 0] in status):
                                flag = 1
                            else:
                                continue
                    if flag:
                        status.remove([build[0], build[1], 0])
                else: 
                    status.remove([build[0], build[1], 0])
        
        # 건축물이 '보'일 경우
        else:
            
            # 설치일 경우
            if build[3] == 1:
                # 설치할 수 있는 조건
                if (([build[0] - 1, build[1], 1] in status) and ([build[0] + 1, build[1], 1] in status)) or ([build[0], build[1] - 1, 0] in status) or ([build[0] + 1, build[1] - 1, 0] in status):
                    status.append([build[0], build[1], 1])
            # 삭제일 경우
            else:
                if ([build[0], build[1] - 1, 0] not in status) and ([build[0] + 1, build[1] - 1, 0] not in status):
                    if ([build[0] - 1, build[1] - 1, 0] in status) and ([build[0] + 2, build[1] - 1, 0] in status):
                        status.remove([build[0], build[1], 1])
                elif ([build[0], build[1] - 1, 0] in status) and ([build[0] + 1, build[1] - 1, 0] in status):
                    status.remove([build[0], build[1], 1])
                else:
                    if [build[0], build[1] - 1, 0] in status:
                        if [build[0] + 1, build[1], 1] in status:
                            if [build[0] + 2, build[1] - 1, 0] in status:
                                status.remove([build[0], build[1], 1])
                            continue
                        if [build[0] + 1, build[1], 0] not in status:
                            status.remove([build[0], build[1], 1])
                    else:
                        if [build[0] - 1, build[1], 1] in status:
                            if [build[0] - 1, build[1] - 1, 0] in status:
                                status.remove([build[0], build[1], 1])
                            continue
                        if [build[0], build[1], 0] not in status:
                            status.remove([build[0], build[1], 1])
                        
    status.sort(key=lambda x:(x[0], x[1], x[2]))
    return status