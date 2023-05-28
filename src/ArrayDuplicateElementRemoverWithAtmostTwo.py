class ArrayDuplicateElementRemoverWithAtmostTwo(object):
    def removeDuplicates(self, nums):
        initial_length = len(nums)
        i = 0
        num = 0
        num_counter = 0
        while(i < initial_length):
            if (i == len(nums)):
                break
            if (i == 0):
                num = nums[0]
                num_counter = 1
                i += 1
                continue
            if (nums[i] != num):
                num = nums[i]
                num_counter = 1
                i += 1
                continue
            if (nums[i] == num):
                num_counter += 1
            if (num_counter > 2):
                nums.pop(i)
                i = i
            else:
                i += 1
                continue
        return len(nums)
            
            