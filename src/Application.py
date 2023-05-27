from src.TreeNode import TreeNode
from src.BinaryTreeInverter import BinaryTreeInverter
from src.BinaryTreeHeightBalanceChecker import BinaryTreeHeightBalanceChecker

def invert_binary_tree():
    left = TreeNode(2, None, None)
    right = TreeNode(4, None, None)
    root = TreeNode(5, left, right)
    
    b = BinaryTreeInverter()
    b.invertTree(root)
    print(root)

invert_binary_tree()
bb = BinaryTreeHeightBalanceChecker()
left = TreeNode(2, None, None)
right = TreeNode(4, None, None)
root = TreeNode(5, left, right)
print(bb.isBalanced(root))