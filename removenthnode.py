def removeNthNode(self,head,n):
    dummy = ListNode(0,head)
    l = dummy
    r = head
    while r and n>0:
        r = r.next
        n -= 1
    while r:
        l = l.next 
        r = r.next 
    l.next = l.next.next 
    return dummy.next
    