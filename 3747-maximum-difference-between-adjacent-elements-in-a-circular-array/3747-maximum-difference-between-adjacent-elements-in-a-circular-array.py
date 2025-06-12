class Solution(object):
    def maxAdjacentDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        N = len(nums)
        maxDist = -float('inf')
        for i in range(N+1):
            if i == N:
                if abs(nums[-1] - nums[0]) > maxDist:
                    maxDist = max(abs(nums[-1] - nums[0]), maxDist)
            else:
                if abs(nums[i] - nums[i-1]) > maxDist:
                    maxDist = max(abs(nums[i] - nums[i-1]), maxDist)

        return maxDist