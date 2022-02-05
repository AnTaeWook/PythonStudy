def solution(s):
    lens = []
    if len(s) <= 1:
        return 1
    for i in range(1, len(s)//2 + 1):
        temp = ''
        count = 1
        for j in range(0, len(s) - i, i):
            if s[j:j + i] != s[j + i:j + 2*i]:
                if count > 1:
                    temp += str(count)
                    count = 1
                temp += s[j:j + i]
                continue
            count += 1
            
        if count > 1:
            temp += str(count)
            temp += s[j:j + i]
        else:
            temp += s[j + i:j + 2*i]
        lens.append(len(temp))
            
    answer = min(lens)
    return answer


# 
###################################################