class Solution:
    def copyRandomList(self, head):

        if head is None:
            return None

        # create copy nodes and add them in orginal list
        curr = head

        while curr:
            copy = Node(curr.val)

            copy.next = curr.next
            curr.next = copy

            curr = copy.next

        # assign random ponter

        curr = head

        while curr:
            copy = curr.next

            if curr.random:
                copy.random = curr.random.next
            
            curr = copy.next

        #separete the curr and orginal list

        curr = head
        copy_head = curr.next

        while curr:
            copy = curr.next

            curr.next = copy.next

            if copy.next:
                copy.next = copy.next.next 

            curr = curr.next
        
        return copy_head




        

        



       



        

    

