class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen = {}

        for i in range(len(nums)):
            curr = nums[i]
            complement = target - curr
            if complement in seen:
                return [seen[complement],i]
            else:
                seen[curr] = i
        
        return None
                
