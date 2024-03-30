# REVERSE THE LINKED LIST WITHIN GIVEN BOUNDARY :
def reverseBetween(self, head, left: int, right: int):
    dummy = ListNode(0, head)

    leftPrev, curr = dummy, head
    for i in range(left - 1):
        leftPrev, curr = curr, curr.next
    
    prev = None
    for i in range(right - left + 1):
        tempNext = curr.next
        curr.next = prev
        prev, curr = curr, tempNext
    
    leftPrev.next.next = curr
    leftPrev.next = prev

    return dummy.next
