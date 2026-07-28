# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        curr = head 

        nodes = []

        while curr:
            nodes.append(curr)
            curr = curr.next

        
        for i in range(0,len(nodes),k):

            if i + k <= len(nodes):
                nodes[i:i+k] = reversed(nodes[i:i+k])

        for i in range(len(nodes)-1):
            nodes[i].next = nodes[i+1]

        nodes[-1].next = None

        return nodes[0]
    


