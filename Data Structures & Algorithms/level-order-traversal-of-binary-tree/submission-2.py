# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.res = []
        def dfs(node, i):
            if not node:
                return
            elif i == len(self.res):
                self.res.append([node.val])
            else:
                self.res[i].append(node.val)
            dfs(node.left, i + 1)
            dfs(node.right, i + 1)
            return
        dfs(root, 0)
        return self.res