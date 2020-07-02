# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        self.nums = 0
        if not root:
            return self.nums
        def helper(stack, node):
            if not node:
                return
            stack.append(node.val)
            if not node.left and not node.right:
                self.nums += int(''.join([str(i) for i in stack]))
            if node.left:
                helper(stack, node.left)
            if node.right:
                helper(stack, node.right)
            stack.pop()
        helper([], root)
        return self.nums