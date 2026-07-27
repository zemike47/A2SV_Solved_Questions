# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        #find middle

        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        
        #reverse the 2nd half 

        second = slow.next
        slow.next = None

        prev = None
        
        while second:
            nxt = second.next
            second.next = prev
            prev = second
            second = nxt
        

        # merge the two halves

        second = prev
        first = head

        while second:
            #save next nodes
            temp1 = second.next
            temp2 = first.next

            #merge two  nodes
            first.next = second
            second.next = temp2

            #advance ptrs
            first = temp2
            second = temp1
            
        


