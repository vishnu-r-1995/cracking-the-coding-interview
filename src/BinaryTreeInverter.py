import src.TreeNode
class BinaryTreeInverter(object):
    def invertTree(self, root):
        if (root is None):
            return None
        if (root.left is None and root.right is None):
            return root
        else:
            left = root.left
            if (root.right != None):
                root.left = self.invertTree(root.right)
            else:
                root.left = None
            if (left != None):
                root.right = self.invertTree(left)
            else:
                root.right = None
            return root
        
 
        