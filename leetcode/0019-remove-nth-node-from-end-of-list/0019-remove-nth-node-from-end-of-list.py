# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        if  head.next is None:
            head = head.next
            return head
        
        curr = head    
        count = 0

        

        while curr:
            count += 1
            curr = curr.next
        
        if n == count:
            return head.next
        
        nth = count - n - 1



        curr = head 
        while nth > 0:
            curr = curr.next
            nth -= 1
        
        if curr.next:
            curr.next = curr.next.next
        else:
            head = head.next

        # res = []
        # while curr:
        #     res.append(curr)
        #     curr = curr.next

        return head