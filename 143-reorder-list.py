def reorderList(head):
    if not head or head.next is None or head.next.next is None:
            return

    def splitList(head):
        slow = fast = head
        while fast:
            fast = fast.next
            if fast:
                fast = fast.next
            else:
                break
            prev = slow
            slow = slow.next
        prev.next = None
        return (head, slow)

    def reverseList(head):
        prev = None
        while head:
            next_node = head.next
            head.next = prev
            prev = head
            head = next_node
        return prev

    def mergeLists(l1, l2):
        while l1 and l2:
            l1_next, l2_next = l1.next, l2.next
            l1.next = l2
            if l1_next:
                l2.next = l1_next
            l1, l2 = l1_next, l2_next

    head_list, tail_list = splitList(head)
    tail_list = reverseList(tail_list)
    mergeLists(head_list, tail_list)
