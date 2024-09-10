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


# CHECK WHETHER LINKED LIST IN BINARY TREE :
def isSubPath(head, root) -> bool:
    def helper(head_node, node):
        if not head_node:
            return True
        if not node or head_node.val != node.val:
            return False
        return  helper(head_node.next, node.left) or helper(head_node.next, node.right)
    if not root:
        return False
    return helper(head, root) or isSubPath(head, root.left) or isSubPath(head, root.right)


# INSERTION OF GCD IN LINKED LIST :
def insertGreatestCommonDivisors(head):
    def find_gcd(a, b):
        if a == 0:
            return b
        return find_gcd(b % a, a)
    # core concept:
    dummy = head
    while dummy and dummy.next:
        slow = dummy
        fast = dummy.next
        # Gcd insertion :
        GCD = find_gcd(slow.val, fast.val)
        result = ListNode(GCD, fast) # type: ignore
        slow.next = result
        # Head traversal ...
        dummy = dummy.next.next
    return head
