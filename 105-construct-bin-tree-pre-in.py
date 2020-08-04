
def buildTree(preorder, intorder):
    if not preorder or not inorder:
        return None
    root = TreeNode(preorder[0])
    root_idx = inorder.index(root.val)
    root.left = self.buildTree(preorder[1:root_idx+1], inorder[:root_idx])
    root.right = self.buildTree(preorder[root_idx+1:], inorder[root_idx+1:])
    return root
