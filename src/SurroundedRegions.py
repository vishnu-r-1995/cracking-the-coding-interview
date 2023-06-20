class SurroundedRegions(object):
    dfs_map = {}
    def solve(self, board):
        for i in range(len(board)):
            for j in range(len(board[i])):
                val = board[i][j]
                if (val == 'X'):
                    continue
                else:
                    self.dfs_map = {}
                    if (self.dfs(board, i, j)):
                        board[i][j] = 'X'
                    
                            
    def dfs(self, board, i, j):
        self.dfs_map[str(i) + str(j)] = 'O'
        for x in range(4):
                try:
                    if (x == 0):
                        if (i - 1 < 0 or j < 0):
                            return False
                        if (board[i-1][j] == 'X'):
                            continue
                        if (str(i-1) + str(j) in self.dfs_map.keys()):
                            continue
                        if (not self.dfs(board, i-1, j)):
                            return False
                    if (x == 1):
                        if (i + 1 < 0 or j < 0):
                            return False
                        if (board[i+1][j] == 'X'):
                            continue
                        if (str(i+1) + str(j) in self.dfs_map.keys()):
                            continue
                        if (not self.dfs(board, i+1, j)):
                            return False
                    if (x == 2):
                        if (i < 0 or j - 1 < 0):
                            return False
                        if (board[i][j-1] == 'X'):
                            continue
                        if (str(i) + str(j-1) in self.dfs_map.keys()):
                            continue
                        if (not self.dfs(board, i, j-1)):
                            return False
                    if (x == 3):
                        if (i < 0 or j + 1 < 0):
                            return False
                        if (board[i][j+1] == 'X'):
                            continue
                        if (str(i) + str(j+1) in self.dfs_map.keys()):
                            continue
                        if (not self.dfs(board, i, j+1)):
                            return False
                except:
                    return False    
        return True                               
            