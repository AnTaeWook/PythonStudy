import bisect as bs

def solution(words, queries):
    answer = []

    # 중복된 쿼리를 위한 메모이제이션
    answer_dic = {}
    
    # 탐색 중 동일 길이와 문자열 위치를 빨리 찾아내기 위한 정렬
    lens = []
    backwords = []
    words.sort(key=lambda x: (len(x), x))
    for w in words:
        lens.append(len(w))
        backwords.append(w[::-1])
    backwords.sort(key=lambda x: (len(x), x))
    
    # 쿼리문을 순회
    for q in queries:
        # 메모이제이션 확인
        if q in answer_dic:
            answer.append(answer_dic[q])
            continue
            
        # '?'가 접두사인 경우
        if q[0] == '?':
            sliced_words = backwords[bs.bisect_left(lens, len(q)):bs.bisect_right(lens, len(q))]
            # 전부 와일드카드인 경우
            if q[-1] == '?':
                count = len(sliced_words)
            else:
                rq = q[::-1]
                left = bs.bisect_left(sliced_words, rq)
                right = bs.bisect_left(sliced_words, rq.replace('?', '}'))
                count = right - left
            answer.append(count)
            answer_dic[q] = count
        
        # '?'가 접미사인 경우
        else:
            sliced_words = words[bs.bisect_left(lens, len(q)):bs.bisect_right(lens, len(q))]
            left = bs.bisect_left(sliced_words, q)
            right = bs.bisect_left(sliced_words, q.replace('?', '}'))
            count = right - left
            answer.append(count)
            answer_dic[q] = count
    
    return answer

# 정답에선 단어 등장 개수를 구하는 함수를 따로 구현하였음
# bisect의 사용 범위 인지하기