def sortList(head):

    def splitList(head):
        if not head:
            return
        slow = head
        fast = head.next
        while fast:
            fast = fast.next
            if fast:
                fast = fast.next
                slow = slow.next
        l2 = slow.next
        slow.next = None
        return (head, l2)

    def mergeLists(l1, l2):
        dummy = cur = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        cur.next = l1 or l2
        return dummy.next
    
    if not head or not head.next:
        return head
    l1, l2 = splitList(head)
    l1 = sortList(l1)
    l2 = sortList(l2)
    head = mergeLists(l1, l2)
    return head