class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        length = 0
        tmp = head
        
        while tmp:
            length += 1
            tmp = tmp.next
                    
        for _ in range(length//2):
            head = head.next
        
        return head