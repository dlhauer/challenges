def numComponents(head, G):
    G = set(G)
    front = follow = head
    count = 0
    while front:
        if front.val not in G:
            if front != follow:
                count += 1
            front = front.next
            follow = front
        else:
            front = front.next
    return count + (front != follow)