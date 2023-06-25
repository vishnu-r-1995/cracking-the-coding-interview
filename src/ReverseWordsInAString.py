class ReverseWordsInAString(object):
    def reverseWords(self, s):
        s = s.strip()
        if (s == ''):
            return s
        word = ''
        l = []
        for x in s:
            if (x.isspace()):
                if (len(word) > 0):
                    l.append(word)
                word = ''
                continue
            word += str(x)
        if (len(word) > 0):
            l.append(word)
        l.reverse()
        return ' '.join(l)
                
            
