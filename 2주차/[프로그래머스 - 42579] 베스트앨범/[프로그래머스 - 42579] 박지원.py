def solution(genres, plays):
    answer = []
    g_dict = {} #(장르명 : 총 재생횟수)
    p_dict = {} #(장르명 : (고유번호, 재생횟수), (고유번호, 재생횟수))
    
    for i in range(len(genres)):
        g_dict[genres[i]] = g_dict.get(genres[i],0) + plays[i]
        if genres[i] not in p_dict:
            p_dict[genres[i]] = [(i,plays[i])]
        else:
            p_dict[genres[i]].append((i,plays[i]))
    
    # 총 재생횟수 기준으로 정렬
    g_dict= sorted(g_dict.items(), key = lambda x:x[1], reverse=True)
    #g_dict= sorted(g_dict.items(), key=operator.itemgetter(0))
    
    for (gen,plays) in g_dict:
        for (i,p) in sorted(p_dict[gen], key=lambda x:x[1], reverse=True)[:2]:
            answer.append(i)
    
    return answer