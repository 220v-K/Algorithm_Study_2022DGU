def solution(clothes):
    dict = {}
    for clo, clo_type in clothes:
        dict[clo_type] = dict.get(clo_type,0)+1 
        # 해당 키를 가진 딕셔너리가 있는 경우 가져옴
        # 해당 키를 가진 딕셔너리가 없는경우 0을 대입함 
    
    case = 1
    for clo_type in dict:
        case *= (dict[clo_type]+1) # 각각 입는 경우+안 입는 경우
    
    answer = case-1 #아무것도 안입는 경우 제외
    return answer