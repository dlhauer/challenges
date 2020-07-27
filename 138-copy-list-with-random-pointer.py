def copyRandomList(head):
    cur = head
    while cur:
        nxt = cur.next
        cur.next = Node(cur.val, nxt)
        cur = cur.next.next
    dummy = Node(0, head)
    dub_prev, prev, cur = dummy, head, head.next
    while prev:
        cur.random = prev.random.next if prev.random else None
        prev = cur.next
        dub_prev.next = cur
        dub_prev = cur
        if prev:
            cur = cur.next.next
    return dummy.next
