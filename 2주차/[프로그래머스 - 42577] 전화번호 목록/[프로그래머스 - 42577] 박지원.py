def solution(phone_book):
    answer = True
    
    #정렬하면 바로 다음 번호만 비교하면 됨
    phone_book.sort() 
    
    for i in range(len(phone_book)-1):
        # i번째 전화번호와 i+1번째 전화번호를 비교하는데, i번째 전화번호길이만큼만 가져와서 비교
        if phone_book[i] == phone_book[i+1][:len(phone_book[i])]:
            return False
        
    return answer