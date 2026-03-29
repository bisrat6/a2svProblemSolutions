class Solution:
    def constructFromPrePost(self, preorder, postorder):
        if not preorder:
            return None
        
        root = TreeNode(preorder[0])
        # If there's only one node, return it
        if len(preorder) == 1:
            return root
        
        # Find the left subtree size using the next value in preorder
        left_size = postorder.index(preorder[1]) + 1
        
        # Recursively build left and right subtrees
        root.left = self.constructFromPrePost(preorder[1:left_size+1], postorder[:left_size])
        root.right = self.constructFromPrePost(preorder[left_size+1:], postorder[left_size:-1])
        
        return root