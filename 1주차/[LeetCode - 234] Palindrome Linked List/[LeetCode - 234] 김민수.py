# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        isPalindrome=True
        
        temp=head
        deq=deque()
        while (temp):
            deq.append(temp.val)
            temp=temp.next

        while len(deq)>1:
            if not deq.popleft()==deq.pop():
                isPalindrome=False
                return isPalindrome 
        
        return isPalindrome


