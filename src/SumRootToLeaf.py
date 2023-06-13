class SumRootToLeaf(object):
    def sumNumbers(self, root):
        lst = self.dfs(root)
        num = 0
        for l in lst:
            l.reverse()
            s = "".join(l)
            num += int(s)
        return num        
            
        return 0
    def dfs(self, root):
        if (root is None):
            l1 = []
            return [l1]
        lst = []
        left_list = self.dfs(root.left)
        right_list = self.dfs(root.right)
        for l in left_list:
            if l:
                l.append(str(root.val))
        for l in right_list:
            if l:
                l.append(str(root.val))
        for l in left_list:
            if l:
                lst.append(l)
        for l in right_list:
            if l:
                lst.append(l)
        if (root.left is None and root.right is None):
            lst.append([str(root.val)])
        return lst