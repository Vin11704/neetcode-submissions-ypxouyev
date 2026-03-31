# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # if root is None:
        #     return root
        # q = [(root)]
        # while q:
        #     curr_node = q.pop(0)
            
        #     curr_node.left, curr_node.right = curr_node.right, curr_node.left
        #     if curr_node.left:
        #         q.append(curr_node.left)
        #     if curr_node.right:
        #         q.append(curr_node.right)
  
        # DFS
        # if root is None:
        #     return root
        # root.left, root.right = root.right, root.left
        # self.invertTree(root.left)
        # self.invertTree(root.right) 

        # stack DFS
        if not root:
            return None
        stack = [root]
        while stack:
            node = stack.pop()
            node.left, node.right = node.right, node.left
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return root
