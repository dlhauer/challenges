def connect(root):
    if root and root.left and root.right:
        root.left.next = root.right
        if root.next:
            root.right.next = root.next.left
        connect(root.left)
        connect(root.right)
    return root