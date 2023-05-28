class ArrayRotator2(object):
    def rotate(self, nums, k):
        len_of_array = len(nums)
        temp = nums[:]
        counter = 0
        if (k == len_of_array):
            return nums
        if (k > len_of_array):
            k = k % len_of_array
        for x in nums:
            if (counter < k):
                nums[counter] = temp[len_of_array - k + counter]
            else:
                nums[counter] = temp[counter - k]
            counter += 1
        return nums