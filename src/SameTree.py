from src.TreeNode import TreeNode
class SameTree(object):
    def isSameTree(self, p, q):
        isSameTree = self.dfs(p, q)
        return isSameTree
    def dfs(self, p, q):
        if (p is None and q is None):
            return True
        if (p is None or q is None):
            return False
        if (p.val == q.val and self.dfs(p.right, q.right) and self.dfs(p.left, q.left)):
            return True
        else:
            return False
            
            