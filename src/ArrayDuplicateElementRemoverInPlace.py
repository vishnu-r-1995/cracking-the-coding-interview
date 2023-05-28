class ArrayDuplicateElementRemoverInPlace(object):
    def removeDuplicates(self, nums):
        num = 0
        i = 0
        length_of_array = len(nums)
        while i < length_of_array:
            if (i == len(nums)):
                break
            if (i == 0):
                num = nums[i]
                i = i + 1
                continue
            if (nums[i] != num):
                num = nums[i]
                i = i + 1
                continue
            nums.pop(i)
            i = i
        return len(nums)