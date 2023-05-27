class BinaryTreePathAnalyzer(object):
    def binaryTreePaths(self, root):
        self.leaf = []
        target_list = []
        result_list = []
        leaf_list = []
        self.getLeafNodes(root)
        [target_list.append(x) for x in self.getPathStr(root) if x not in target_list]
        while("" in target_list):
            target_list.remove("")
        for x in target_list:
            for y in self.leaf:
                if (x.startswith(str(root.val)) and x.endswith(str(y))):
                    result_list.append(x)
        for l in self.leaf:
            print(l)
        return result_list
        
    def getPathStr(self, root):
        path_list = ['']
        if (root is None):
            return path_list
        for x in self.getPathStr(root.right):
            if (x != ''):
                path_list.append(str(root.val) + "->" + x)
            else:
                path_list.append(str(root.val))
        for y in self.getPathStr(root.left):
            if (y != ''):
                path_list.append(str(root.val) + "->" + y)
            else:
                path_list.append(str(root.val))
        return path_list
    
    def getLeafNodes(self, root):
        if (root != None and root.left == None and root.right == None):
            self.leaf.append(root.val)
            return
        elif (root is None):
            return
        else:
            self.getLeafNodes(root.left)
            self.getLeafNodes(root.right)
            return
        