from src.TreeNode import TreeNode
from src.BinaryTreeInverter import BinaryTreeInverter
from src.BinaryTreeHeightBalanceChecker import BinaryTreeHeightBalanceChecker
from src.BinaryTreePathAnalyzer import BinaryTreePathAnalyzer
from src.ArrayElementRemover import ArrayElementRemover
from src.ArrayDuplicateElementRemoverInPlace import ArrayDuplicateElementRemoverInPlace
from src.ArrayDuplicateElementRemoverWithAtmostTwo import ArrayDuplicateElementRemoverWithAtmostTwo
from src.MajorityElementFinder import MajorityElementFinder
from src.ArrayRotator import ArrayRotator
from src.ArrayRotator2 import ArrayRotator2
from src.StockBuySellManager import StockBuySellManager
from src.StockBuySellManager2 import StockBuySellManager2
from src.JumpGame import JumpGame
from src.RansomNoteGenerator import RansomNoteGenerator
from src.HIndex import HIndex
from src.GasStationVisitor import GasStationVisitor

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

arr2 = [1,2,3,4,5,6,7]
def callArrayRotator():
    ar = ArrayRotator()
    arr = ar.rotate(arr2, 6)
    print(arr)
    
def callArrayRotator2():
    ar2 = ArrayRotator2()
    arr = ar2.rotate(arr2, 3)
    print(arr)

prices = [7,1,5,3,6,4]

def callStockBuySellManager():
    sbsm = StockBuySellManager()
    max_profit = sbsm.maxProfit(prices)
    print("Stock Buy Sell Manager - Maximum Profit:", max_profit)
    
def callStockBuySellManager2():
    sbsm2 = StockBuySellManager2()
    max_profit = sbsm2.maxProfit(prices)
    print("Stock Buy Sell Manager 2 - Maximum Profit:", max_profit)
    
nums = [3,2,1,0,4]
def callJumpGame():
    jg = JumpGame()
    can_reach_last = jg.canJump(nums)
    print("Jump Game - Can Reach Last Position?:", str(can_reach_last))

ransomNote = 'aa'
magazine = 'aab'
def callRansomNoteGenerator():
    rng = RansomNoteGenerator()
    can_create_ransom_note = rng.canConstruct(ransomNote, magazine)
    print("Ransom Note - Can create ransom note?:", str(can_create_ransom_note))

citations = [3,0,6,1,5]
def callHIndex():
    hi = HIndex()
    h_index = hi.hIndex2(citations)
    print("H-Index - H Index of the researcher:", str(h_index))

gas = [1,2,3,4,5]
cost = [3,4,5,1,2]
def callGasStationVisitor():
    gsv = GasStationVisitor()
    index_to_start = gsv.canCompleteCircuit2(gas, cost)
    print("Gas Station - Index to start to complete circuit around gas stations:", str(index_to_start))
    
callGasStationVisitor()