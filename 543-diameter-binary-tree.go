package main

var maxD int = 0

func diameterOfBinaryTree(root *TreeNode) int {
	helper(root, 0)
	return maxD
}

func helper(root *TreeNode, depth int) int {
	if root == nil {
		return depth - 1
	}
	left := helper(root.Left, depth+1)
	right := helper(root.Right, depth+1)
	d := left + right - (2 * depth)
	if d > maxD {
		maxD = d
	}
	if left > right {
		return left
	}
	return right
}
