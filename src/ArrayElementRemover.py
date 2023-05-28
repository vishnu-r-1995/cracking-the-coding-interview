class ArrayElementRemover(object):
    def removeElement(self, nums, val):
        while val in nums:
            nums.remove(val)
        return len(nums)