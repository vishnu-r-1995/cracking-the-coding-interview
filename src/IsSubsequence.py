class IsSubsequence(object):
    def isSubsequence(self, s, t):
        if (s.strip() == ""):
            return True
        s_chars = [x for x in s]
        s_chars_counter = 0
        t_chars = [x for x in t]
        for i in range(len(t_chars)):
            t_str = str(t_chars[i])
            if (str(s_chars[s_chars_counter]) == t_str):
                if (s_chars_counter + 1 == len(s_chars)):
                    return True
                else:
                    s_chars_counter += 1
        return False
