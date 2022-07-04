# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        a = []
        tmp1 = 0
        tmp2 = 0
        
        node = head
        while node.next: ## next가 null이 아닐때 까지
            a.append(node.val)
            node = node.next
        a.append(node.val) #마지막 노드값 추가 

        
        for i in range(0,int(len(a)/2)):# 양끝에서 하나씩 빼서 동일여부 확인 
            tmp1 = a.pop(0)
            tmp2 = a.pop()
            if tmp1 != tmp2:
                return False
            
        return True