# REMOVE THE NTH NODE FROM THE END OF THE LINKED LIST :
def removeNthFromEnd(head, n: int):
    if not head:
        return 
    dummy = ListNode() # type: ignore
    dummy.next = head
    A = B = dummy
    for _ in range(n + 1):
        A = A.next
    while A:
        A = A.next
        B = B.next
    B.next = B.next.next
    return dummy.next
        