# Definition for a binary tree node.
# class TreeNode:
#     def _init_(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode | None) -> int:
        self.result=float('-inf')
        def dfs(node):
            if node is None:
                return 0
            left=max(0,dfs(node.left))
            right=max(0,dfs(node.right))
            sifat=node.val+left+right
            self.result=max(self.result,sifat)
            return node.val+max(left,right)
        dfs(root)
        return self.result   