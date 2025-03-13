class Solution(object):
    def minZeroArray(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: int
        """
        if not self.toZero(nums,queries):
            return -1

        l, r = 0, len(queries)

        while l < r:
            m = (l + r) // 2
            if self.toZero(nums,queries[:m]):
                r = m
            else:
                l = m + 1
        return l 
    
    def toZero(self,nums,queries):
        diff = [0 for num in nums] + [0]

        for i in range(len(queries)):
            lidx, ridx, val = queries[i]

            diff[lidx] += val
            diff[ridx + 1] -= val
        
        ac = 0
        for j in range(len(nums)):
            ac += diff[j]
            if ac < nums[j]:
                return False
        
        return True