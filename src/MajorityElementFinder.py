class MajorityElementFinder(object):
    def majorityElement(self, nums):
        element_count_dict = {}
        for x in nums:
            count = element_count_dict.get(x)
            if (count is None):
                element_count_dict[x] = 1
            else:
                count += 1
                element_count_dict[x] = count
        majority_element = max(zip(element_count_dict.values(), element_count_dict.keys()))[1]
        return majority_element
            
            