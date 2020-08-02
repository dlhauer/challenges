def isValidBST(root, min_val=float('-inf'), max_val=float('inf')):
    if not root:
        return True
    if root.val <= min_val or root.val >= max_val:
        return False
    left  = isValidBST(root.left, min_val, root.val)
    right = isValidBST(root.right, root.val, max_val)
    return left and right
