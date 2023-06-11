class MaximumDepthOfBinaryTree(object):
    counter = 0
    def maxDepth(self, root):
        counter = 0
        self.dfs(root, counter)
        return self.counter
    def dfs(self, root, counter):
        if (root is None):
            return
        counter += 1
        if (self.counter < counter):
            self.counter = counter
        self.dfs(root.right, counter)
        self.dfs(root.left, counter)
        return