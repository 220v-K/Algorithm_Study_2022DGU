# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        list_length=0
        temp=head
        
        while temp is not None:
            temp=temp.next
            list_length+=1
        
        for i in range(list_length/2):
            head=head.next
       
        return head
