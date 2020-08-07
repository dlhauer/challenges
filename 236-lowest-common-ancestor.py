def lowestCommonAncestor(root, p, q):
    
    def get_path(root, target_node, path=[]):
        if root == target_node:
            return path + [root]
        if not root:
            return None
        left = get_path(root.left, target_node, path+[root])
        right = get_path(root.right, target_node, path+[root])
        return left or right

    p_path = get_path(root, p)
    q_path = get_path(root, q)
    for i in range(min(len(p_path), len(q_path))):
        if p_path[i] == q_path[i]:
            res = p_path[i]
        else:
            break
    return res
