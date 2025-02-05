class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        numLen = len(nums)
        ans = []
        for i in range(numLen):
            seen = set()
            icurr = nums[i]
            j = i + 1
            while j < numLen:
                jcurr = nums[j]
                target = 0 - icurr - jcurr
                if target in seen:
                    trip = [icurr,jcurr,target]
                    trip.sort()
                    if trip not in ans:               
                        ans.append(trip)
                seen.add(jcurr)
                j += 1

        return ans

        