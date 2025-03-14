class Solution(object):
    def maximumCount(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        neg = self.bin_search(nums,0)
        pos = len(nums) - self.bin_search(nums,1)
        return max(neg,pos)

    def bin_search(self, nums, mt):
        l, r = 0, len(nums) - 1
        bound = len(nums)
        while l <= r:
            m = l + (r - l) // 2
            if nums[m] >= mt:
                r = m - 1
                bound = m
            else:
                l = m + 1

        return bound

            

        
