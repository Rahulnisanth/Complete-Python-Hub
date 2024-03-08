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


# ADDITION OF TWO LINKED-LISTS :
def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    dummy = ListNode()
    result = dummy
    total = carry = 0

    while l1 or l2 or carry:
        total = carry
        if l1:
            total += l1.val
            l1 = l1.next
        if l2:
            total += l2.val
            l2 = l2.next
        
        num = total % 10
        carry = total // 10
        dummy.next = ListNode(num)
        dummy = dummy.next
    
    return result.next