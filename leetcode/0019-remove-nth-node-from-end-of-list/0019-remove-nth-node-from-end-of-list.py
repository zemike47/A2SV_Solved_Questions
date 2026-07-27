# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
          
       
        dummy = ListNode()
        dummy.next = head


        count = 0
        curr = head

        while curr:
            curr = curr.next
            count += 1


        # print(count)
        curr = dummy

        for _ in range(count-n):
            curr = curr.next


        curr.next = curr.next.next

        return dummy.next
        
