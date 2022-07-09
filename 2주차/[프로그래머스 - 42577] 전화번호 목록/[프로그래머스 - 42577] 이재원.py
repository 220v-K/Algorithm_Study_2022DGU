def solution(phone_book):
    set_book = set(phone_book)

    for phone in phone_book:
        number = ""
        for num in phone:
            number += num
            if number in set_book and number != phone:
                return False
    return True
