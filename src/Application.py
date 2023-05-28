from src.TreeNode import TreeNode
from src.BinaryTreeInverter import BinaryTreeInverter
from src.BinaryTreeHeightBalanceChecker import BinaryTreeHeightBalanceChecker
from src.BinaryTreePathAnalyzer import BinaryTreePathAnalyzer
from src.ArrayElementRemover import ArrayElementRemover
from src.ArrayDuplicateElementRemoverInPlace import ArrayDuplicateElementRemoverInPlace
from src.ArrayDuplicateElementRemoverWithAtmostTwo import ArrayDuplicateElementRemoverWithAtmostTwo
from src.MajorityElementFinder import MajorityElementFinder

left = TreeNode(2, None, None)
right = TreeNode(4, None, None)
root = TreeNode(5, left, right)
    
def invert_binary_tree(root):
    b = BinaryTreeInverter()
    b.invertTree(root)

def callBinaryTreeHeightBalanceChecker(root):
    bb = BinaryTreeHeightBalanceChecker()
    print(bb.isBalanced(root))

def callBinaryTreePathAnalyzer(root):
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
    
def callArrayDuplicateElementRemoverWithAtmostTwo():
    ader2 = ArrayDuplicateElementRemoverWithAtmostTwo()
    len_of_array_after_duplicate_removal = ader2.removeDuplicates(arr)
    print("Array Duplicate Element Remover 2:", len_of_array_after_duplicate_removal)
    
def callMajorityElementFinder():
    mef = MajorityElementFinder()
    val = mef.majorityElement(arr)
    print(val)

callMajorityElementFinder()