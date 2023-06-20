class ClimbingStairs(object):
    self.dp_map = {}
    def climbStairs(self, n):
        return self.dp(n)
    def dp(self, n):
        if (n == 1):
            return 1
        elif (n == 2):
            return 2
        else:
            if (n - 2 not in self.dp_map.keys()) :
                dp_n_minus_2 = self.dp(n-2)
                self.dp_map[n-2] = dp_n_minus_2
            if (n - 1 not in self.dp_map.keys()) :
                dp_n_minus_1 = self.dp(n-1)
                self.dp_map[n-1] = dp_n_minus_1
            return self.dp.get(n-2) + self.dp.get(n-1)
