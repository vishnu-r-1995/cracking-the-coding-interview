class RomanToInteger(object):
    def romanToInt(self, s):
        roman_chars = [x for x in s]
        left_pointer = 0
        right_pointer = 1
        roman_map = {'I':1, 'IV':4, 'V':5, 'IX':9, 'X':10, 'XL':40, 'L':50, 
                     'XC':90, 'C':100, 'CD':400, 'D':500, 'CM':900, 'M':1000}
        value = 0
        while left_pointer < len(roman_chars):
            left_value = roman_chars[left_pointer]
            if (right_pointer < len(roman_chars)):
                right_value = roman_chars[right_pointer]
                combined_value = str(left_value) + str(right_value)
                if (roman_map.get(combined_value) is not None):
                    value += roman_map.get(combined_value)
                    left_pointer += 2
                    right_pointer += 2
                    continue
            if (roman_map.get(str(left_value)) is not None):
                value += roman_map.get(left_value)
                left_pointer += 1
                right_pointer += 1
        return value
