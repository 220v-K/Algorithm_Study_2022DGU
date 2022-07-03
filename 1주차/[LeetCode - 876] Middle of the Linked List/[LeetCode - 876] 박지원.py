# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        cnt = 1
        node = head
        while node.next:    ## 리스트 길이 확인
            cnt += 1
            node = node.next
        
        node = head
        for i in range(0, int(cnt/2)): ## 리스트 절반길이만큼 이동
            node = node.next
            
        return node