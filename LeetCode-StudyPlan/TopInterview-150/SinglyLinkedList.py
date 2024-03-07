# DETECT THE CYCLE OF THE LINKED LIST :
def hasCycle(self, head: Optional[ListNode]) -> bool:
    # Drive function...
    def detectCycle(prev, curr):
        if curr == None or curr.next == None:
            return False
        if prev == curr:
            return True
        return detectCycle(prev.next, curr.next.next)
    
    if head == None or head.next == None:
        return False
    
    return detectCycle(head, head.next)


# FIND THE MIDDLE ELEMENT OF THE GIVEN LINKED LIST :
def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
    curr, count = head, 0
    while curr != None:
        count += 1
        curr = curr.next
    curr = head
    for i in range(count//2):
        curr = curr.next
    return curr