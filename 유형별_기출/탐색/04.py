def solution(p):
    # 빈 문자열일 경우 빈 문자열 리턴
    if p == '':
        return ''
    
    check = 0
    isRight = True
    u = []
    # 검사하여 균형잡힌 괄호 문자열로 분리
    for i in range(len(p)):
        if p[i] == '(':
            check += 1
        else:
            check -= 1
        if check == 0:
            u = p[:i + 1]
            v = p[i + 1:]
            break
        # 올바르진 않음
        if check < 0:
            isRight = False

    # 올바르지 않으면 제시된 알고리즘 실행
    if not isRight:
        t = ''
        u = u[1:-1]
        for c in u:
            if c == '(':
                t += ')'
            else:
                t += '('
        return '(' + solution(v) + ')' + t

    # 올바른 괄호면 그대로 실행
    return u + solution(v)

# 문제에선 균형잡힌 괄호 문자열의 인덱스 반환과 올바른 괄호 문자열인지 판단하는 함수를 solution함수 밖에서 따로 구현함