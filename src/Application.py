from src.TreeNode import TreeNode
from src.BinaryTreeInverter import BinaryTreeInverter
from src.BinaryTreeHeightBalanceChecker import BinaryTreeHeightBalanceChecker
from src.BinaryTreePathAnalyzer import BinaryTreePathAnalyzer
from src.ArrayElementRemover import ArrayElementRemover
from src.ArrayDuplicateElementRemoverInPlace import ArrayDuplicateElementRemoverInPlace

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

btp = BinaryTreePathAnalyzer()
btp.binaryTreePaths(root)
arr = [1,2,2,3,3,3,4,5]

def callArrayElementRemover():
    val = 3
    aer = ArrayElementRemover()
    num_of_elements_other_than_removed = aer.removeElement(arr, 3)
    print("Array Element Remover:", num_of_elements_other_than_removed)

def callArrayDuplicateElementRemoverInPlace():
    ader = ArrayDuplicateElementRemoverInPlace()
    len_of_array_after_duplicate_removal = ader.removeDuplicates(arr);
    print("Array Duplicate Element Remover:", len_of_array_after_duplicate_removal)
    
callArrayDuplicateElementRemoverInPlace()