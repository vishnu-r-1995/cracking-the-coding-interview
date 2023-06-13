class ValidPalindrome(object):
    def isPalindrome(self, s):
        s = s.lower()
        left = 0
        right = len(s) - 1
        while (left != right):
            if (left == len(s)):
                break
            if (right < 0):
                break
            if (not s[left].isalnum()):
                left += 1
                continue
            if (not s[right].isalnum()):
                right -= 1
                continue
            if (s[left] != s[right]):
                return False
            left += 1
            right -= 1
        return True