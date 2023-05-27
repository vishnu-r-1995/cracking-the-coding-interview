class ArrayMergeAndSort(object):
    def merge(self, nums1, m, nums2, n):
        for i, x in enumerate(nums1):
            if (i >= m):
                nums1[i] = nums2[i - m]
        nums1.sort()
