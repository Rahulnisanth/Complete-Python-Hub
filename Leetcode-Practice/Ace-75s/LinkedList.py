# DELETE THE MIDDLE OF THE LINKED LIST :
def deleteMiddle(head):
    if not head: 
        return
    if not head.next:
        return 
    slow = head
    fast = head
    temp = head
    while fast and fast.next:
        temp = slow
        slow = slow.next
        fast = fast.next.next
    temp.next = slow.next
    return head


# REVERSE THE GIVEN LINKED LIST :
def reverseList(head):
    if not head:
        return 
    if not head.next:
        return head
    curr = head
    prev = None
    while curr:
        fast = curr.next
        curr.next = prev
        prev = curr
        curr = fast
    return prev