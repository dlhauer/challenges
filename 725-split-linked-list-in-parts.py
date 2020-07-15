def splitListToParts(root, k):
    head = root; length = 0
    while head:
        length += 1
        head = head.next
    sub_len, extras = divmod(length, k)
    front = follow = root; i = 0; res = []
    while front:
        i += 1
        if (extras > 0 and i == sub_len+1
            or extras <= 0 and i == sub_len):
            extras -= 1
            res.append(follow)
            follow = front.next
            front.next = None
            front = follow
            i = 0
        else:
            front = front.next
    for _ in range(k-length):
        res.append(None)
    return res
