# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def inorder(node):
            if not node:
                return
        
            # check if there is left
            inorder(node.left)
            # set to arr when there is no child left
            res.append(node.val)
            # check if there is right
            inorder(node.right)

        inorder(root)
        return res
        
    
    """
    # pattern used -> DFS (depth first search)
        1
        /\
       2  5
       /\
      3  4

      res = [3,2,4,1,5]
      - find the most left (left and lowest)
      - then its node
      - then if there is right (same node)
      *** priority -> left > node > right
      - then check again in higher node (recursive)

      start
      - create function to check node and its children
      - create arr to store the result
      - check follow left-node-right
      - then add node.val to arr
      *** the last one won't have left/right

      # start
            2    -> node.val
            /\
           3  4
    node.left|node.right

            2
            /\
   node -> 3  4
   node.left = None, node.right = None, 
   node.val = 3 -> store this in array

      def inorder(node):
        if not node:
            return

        inorder(node.left)
        arr.append(node.val) # set arr on this
        inorder(node.right) # 
    """