class PlusOneSolver(object):
    def plusOne(self, digits):
        new_digits = []
        counter = 0
        large_number = 0
        digits.reverse()
        for cnt, x in enumerate(digits):
            large_number += x * pow(10, cnt)
        large_number += 1
        while(large_number >= 1):
            new_digits.insert(counter, large_number%10)
            counter += 1
            large_number = int(large_number/10)
        new_digits.reverse()
        return new_digits
            
