# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # DFS
        # if root is None:
        #     return 0
        # else:
        #     left = self.maxDepth(root.left)
        #     right = self.maxDepth(root.right)
        #     max_depth = max(left, right) + 1
        # return max_depth
            
        # BFS
        max_depth = 1
        if root is None:
            return 0     
        else:
            ls = []
            ls.append((root, 1))
            while ls:
                curr_node, depth = ls.pop(0)
                if curr_node.left:
                    ls.append((curr_node.left, depth+1))
                    max_depth = max(max_depth, depth+1)
                if curr_node.right:
                    ls.append((curr_node.right, depth+1))
                    max_depth = max(max_depth, depth+1)
        return max_depth
                


