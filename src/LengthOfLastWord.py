class LengthOfLastWord(object):
    def lengthOfLastWord(self, s):
        s = s.strip()
        counter = 0
        i = 0
        while (i < len(s)):
            if (s[i].isspace()):
                counter = 0
                i += 1
                continue
            else:
                counter += 1
                i += 1
        return counter
