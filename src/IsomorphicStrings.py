class IsomorphicStrings(object):
    def isIsomorphic(self, s, t):
        mapTo = {}
        s_chars = [x for x in s]
        t_chars = [x for x in t]
        for i, x in enumerate(s_chars):
            if x in mapTo.keys():
                t_char = mapTo[str(x)]
                if (i >= len(t_chars)):
                    return False
                if (t_chars[i] != t_char):
                    return False
            elif (t_chars[i] in mapTo.values()):
                return False
            else:
                if (i >= len(t_chars)):
                    return False
                mapTo[str(x)] = str(t_chars[i])
        return True
