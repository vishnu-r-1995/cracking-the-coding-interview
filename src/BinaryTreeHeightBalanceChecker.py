class BinaryTreeHeightBalanceChecker(object):
    def isBalanced(self, root):
        def getHeight(node):
            if node is None:
                return 0
            left_height = getHeight(node.left)
            right_height = getHeight(node.right)
            if left_height == -1 or right_height == -1 or abs(left_height - right_height) > 1:
                return -1
            return 1 + max(left_height, right_height)
        return getHeight(root) != -1
        
