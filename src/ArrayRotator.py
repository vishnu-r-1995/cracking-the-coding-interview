class ArrayRotator(object):
    def rotate(self, nums, k):
        len_of_array = len(nums)
        if (k == len_of_array):
            return nums
        if (k > len_of_array):
            k = k % len_of_array
        nums = nums[-k :] + nums[0 : -k]
        return nums