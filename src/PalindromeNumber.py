class PalindromeNumber(object):
    def isPalindrome(self, x):
        sum = 0
        number = x
        while (x > 0):
            y = x%10
            x = int(x/10)
            sum = sum*(10) + y
        if (number == sum):
            return True
        else:
            return False
