# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cursor = head
        cntNode = 0
        while cursor != None:
            cntNode += 1
            cursor = cursor.next

        for _ in range(int(cntNode / 2)):
            head = head.next
            
        return head