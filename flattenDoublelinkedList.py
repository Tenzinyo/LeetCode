def flattenDoubleLinkedList(self, head):
    node = head
    while node:
        if node.child:
            temp = node.next 
            node.next = self.flatten(node.child)
            node.next.prev = node
            node.child = None
            while node.next:
                node = node.next 
            node.next = temp
            if temp:
                temp.prev = node
        node = node.next
    return head