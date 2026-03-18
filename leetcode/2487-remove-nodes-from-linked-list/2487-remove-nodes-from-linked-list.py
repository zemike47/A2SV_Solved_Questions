# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverseTheLinkedList(Head):
            curr = Head
            prev = None

            while curr:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            
            return prev
        
        head = reverseTheLinkedList(head)

        max_val = head.val
        curr = head

        while curr and curr.next:
            if curr.next.val < max_val:
                curr.next = curr.next.next

            else:
                curr = curr.next
                max_val = curr.val
        
        return reverseTheLinkedList(head)



