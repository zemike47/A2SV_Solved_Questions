class Solution:
    def copyRandomList(self, head):
        if not head:
            return None

        # Step 1: interleave copied nodes
        curr = head
        while curr:
            new_node = Node(curr.val)
            new_node.next = curr.next
            curr.next = new_node
            curr = new_node.next

        # Step 2: assign random pointers
        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next

        # Step 3: separate the lists
        curr = head
        copy_head = head.next

        while curr:
            copy = curr.next
            curr.next = copy.next
            
            if copy.next:
                copy.next = copy.next.next
            
            curr = curr.next

        return copy_head