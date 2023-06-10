class ValidParentheses(object):
    def isValid(self, s):
        if (len(s) == 1):
            return False
        x1 = [ch for ch in s]
        x2 = []
        while len(x1) > 0:
            x1_str = x1.pop()
            if (len(x2) > 0):
                x2_str = x2.pop()
                if (x2_str == '}' and x1_str == '{'):
                    continue
                elif(x2_str == ']' and x1_str == '['):
                    continue
                elif(x2_str == ')' and x1_str == '('):
                    continue
                x2.append(x2_str)
            x2.append(x1_str)
        if ('(' in x2 and ')' not in x2 or ')' in x2 and '(' not in x2):
            return False
        if ('{' in x2 and '}' not in x2 or '}' in x2 and '{' not in x2):
            return False
        if ('[' in x2 and ']' not in x2 or ']' in x2 and '[' not in x2):
            return False
        x1 = x2[:]
        x1.reverse()
        if (x1 == x2):
            return True
        else:
            return False