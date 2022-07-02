class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        li = []
        
        while head:
            li.append(head.val)
            head = head.next
            
        return li == li[::-1]   ## 뒤집은 리스트와 원 리스트 비교 (리스트 전체에서 인덱스를 1씩 감소시키면서 요소를 가져옴)