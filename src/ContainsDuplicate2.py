class ContainsDuplicate2(object):
    d_map = {}
    def containsNearbyDuplicate(self, nums, k):
        for x in range(len(nums)):
            num = nums[x]
            if num in self.d_map.keys():
                last_occurence = self.d_map[num]
                if (abs(x - last_occurence) <= k):
                    return True
                else:
                    self.d_map[num] = x
            else:
                self.d_map[num] = x
        return False