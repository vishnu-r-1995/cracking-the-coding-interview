class SymmetricTree(object):
    left = {}
    right = {}
    def isSymmetric(self, root):
        level = 1
        self.left[level] = [root.val]
        self.right[level] = [root.val]
        if (root is None):
            return True
        if (root.left is None and root.right is None):
            return True
        else:
            self.dfs(root, level + 1)
        for x in self.left.keys():
            l = self.left[x]
            if (x not in self.right.keys()):
                return False
            else:
                r = self.right[x]
                r.reverse()
                if (l == r):
                    continue
                else:
                    return False
        return True
    def dfs(self, root, level):
        if (root.left is None and root.right is None):
            return
        else:
            if (root.left is not None):
                if (level in self.left.keys()):
                    l = self.left[level]
                    l.append(root.left.val)
                    self.left[level] = l
                else:
                    l = []
                    l.append(root.left.val)
                    self.left[level] = l
            if (root.right is not None):
                if (level in self.right.keys()):
                    l = self.right[level]
                    l.append(root.right.val)
                    self.right[level] = l
                else:
                    l = []
                    l.append(root.right.val)
                    self.right[level] = l
            if (root.left is not None):
                self.dfs(root.left, level + 1)
            if (root.right is not None):
                self.dfs(root.right, level + 1)
            