def removeZeroSumSublists(head):
    dummy = ListNode(0, head)
    stack = []
    pre_map = dict()
    node = dummy
    pre = 0
    while node:
        pre += node.val
        if pre in pre_map:
            pre_map[pre].next = node.next
            while stack[-1] != pre:
                pre_map.pop(stack.pop())
        else:
            pre_map[pre] = node
            stack.append(pre)
        node = node.next
    return dummy.next
