# DELETE NODES FROM THE LINKED LIST PRESENT IN THE ARRAY :
def modifiedList(nums, head):
    if not head:
        return None
    if not nums:
        return head
    num_set = set(nums)
    dummy = ListNode(0) # type: ignore
    dummy.next = head
    curr = dummy
    while curr and curr.next:
        if curr.next.val in num_set:
            curr.next = curr.next.next
        else:
            curr = curr.next
    return dummy.next