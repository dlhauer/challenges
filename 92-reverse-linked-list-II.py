def reverseBetween(head, m, n):

    def reverseUntil(head, num_nodes):
        tail, prev, i = head, None, 0
        while head and i < num_nodes:
            next_node = head.next
            head.next = prev
            prev = head
            head = next_node
            i += 1
        tail.next = head
        return prev

    if m == 1:
        return reverseUntil(head, n)
    cur = head; i = 1
    while m > 1 and i < m-1:
        cur = cur.next
        i += 1
    cur.next = reverseUntil(cur.next, n-i)

    return head
