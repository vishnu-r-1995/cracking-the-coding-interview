class HappyNumber(object):
    def isHappy(self, n):
        sum = self.iter(n)
        while (sum >= 10):
            sum = self.iter(sum)
        if (sum == 1):
            return True
        else:
            return False
        
    def iter(self, n):
        sum = 0
        while (n > 0):
            x = n%10
            sum += x**2
            n = int(n/10)
        return sum
            