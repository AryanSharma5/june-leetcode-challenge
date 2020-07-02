# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        queue = []
        queue.append(root)
        ans = 0
        while queue:
            size = len(queue)
            temp = []
            for i in range(size):
                cur_node = queue.pop(0)
                temp.append(cur_node.val)
                if cur_node.left:
                    queue.append(cur_node.left)
                if cur_node.right:
                    queue.append(cur_node.right)
            #print(temp)
            ans += len(temp)
        return ans