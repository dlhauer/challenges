import collections

def zigzagLevelOrder(root):
    res, cur = [], []
    cur_len = 1
    left_right = True
    q = collections.deque([root])

    while q:
        node = q.pop()
        if not node:
            continue
        if node.left:
            q.appendleft(node.left)
        if node.right:
            q.appendleft(node.right)
        cur.append(node.val)
        if len(cur) == cur_len:
            if not left_right:
                cur.reverse()
            cur_len = len(q)
            res.append(cur)
            cur = []
            left_right = not left_right
    return res
