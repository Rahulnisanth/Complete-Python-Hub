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


# ODD EVEN LINKED LIST :
def oddEvenList(head):
    odd_head = odd = ListNode(0) # type: ignore
    even_head = even = ListNode(0) # type: ignore
    curr = head
    counter = 1
    while curr:
        if counter % 2 == 0:
            even.next = curr
            even = even.next
        else:
            odd.next = curr
            odd = odd.next
        curr = curr.next
        counter += 1
    odd.next = even_head.next
    even.next = None
    return odd_head.next


# MAXIMUM TWIN SUM OF THE LINKED LIST :
def pairSum(head) -> int:
    if not head:
        return 0
    slow = fast = head
    stack = []
    while fast and fast.next:
        stack.append(slow.val)
        slow = slow.next
        fast = fast.next.next
    result = float("-inf")
    while slow:
        result = max(result, stack.pop() + slow.val)
        slow = slow.next
    return result