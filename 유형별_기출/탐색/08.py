from collections import deque
import copy

def get_next_pos(pos, board):
    # 다음 이동할 수 있는 좌표
    next_pos = []
    p1, p2 = pos
    # 이동하는 경우
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    for i in range(len(dx)):
        np1 = copy.deepcopy(p1)
        np2 = copy.deepcopy(p2)
        np1[0] += dx[i]
        np1[1] += dy[i]
        np2[0] += dx[i]
        np2[1] += dy[i]
        # 이동할 수 없으면 추가 불가
        if board[np1[0]][np1[1]] == 1 or board[np2[0]][np2[1]] == 1:
            continue
        next_pos.append((np1, np2))
    # 현재 로봇이 가로로 있는 경우 회전
    if p2[1] - p1[1] == 1:
        if board[p1[0] + 1][p1[1]] == 0 and board[p2[0] + 1][p2[1]] == 0:
            next_pos.append((p2, [p1[0] + 1, p1[1] + 1]))
            next_pos.append((p1, [p2[0] + 1, p2[1] - 1]))
        if board[p1[0] - 1][p1[1]] == 0 and board[p2[0] - 1][p2[1]] == 0:
            next_pos.append(([p1[0] - 1, p1[1] + 1], p2))
            next_pos.append(([p2[0] - 1, p2[1] - 1], p1))
    
    # 현재 로봇이 세로로 있는 경우 회전
    else:
        if board[p1[0]][p1[1] + 1] == 0 and board[p2[0]][p2[1] + 1] == 0:
            next_pos.append((p2, [p1[0] + 1, p1[1] + 1]))
            next_pos.append((p1, [p2[0] - 1, p2[1] + 1]))
        if board[p1[0]][p1[1] - 1] == 0 and board[p2[0]][p2[1] - 1] == 0:
            next_pos.append(([p1[0] + 1, p1[1] - 1], p2))
            next_pos.append(([p2[0] - 1, p2[1] - 1], p1))
        
    return next_pos

def solution(board):
    # 보드의 4면에 벽 하나씩 더 치기
    n = len(board)
    temp_board = [[1]*(n + 2)]
    for i in range(n):
        temp_line = [1] + board[i] + [1]
        temp_board.append(temp_line)
    temp_board.append([1]*(n + 2))
    board = copy.deepcopy(temp_board)
    n = len(board)
    
    # 방문 여부
    visited = []
    depth = 0
    
    # bfs
    start_pos = ([1, 1], [1, 2])
    visited.append(start_pos)
    queue = deque([(start_pos, depth)])
    while queue:
        p, d = queue.popleft()
        print(p, d)
        # 도착지에 도착한 경우
        if [n - 2, n - 2] in p:
            return d

        nps = get_next_pos(p, board)
        for np in nps:
            if np not in visited:
                queue.append((np, d + 1))
                visited.append(np)

# BFS로 최단경로를 구하는 문제지만 로봇이 두칸을 차지하기 때문에 이동할 수 있는 좌표를
# 구하는 함수를 구현하여 사용하며 풀어야 함