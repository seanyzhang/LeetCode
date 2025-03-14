class Solution(object):
    def maximumCandies(self, candies, k):
        """
        :type candies: List[int]
        :type k: int
        :rtype: int
        """
        biggest = max(candies)

        l, r = 1, biggest
        best = 0
        m = 0

        if not self.check(candies, k, 1):
            return m
        
        while l <= r:
            m = l + (r - l) // 2

            if self.check(candies, k, m):
                l = m + 1
                best = m
            
            else:
                r = m - 1
        
        return best

        

    def check(self, candies, k, val):
        total = 0
        for i in range(len(candies)):
            quotient = candies[i] // val
            total += quotient

        if total >= k:
            return True
        else:
            return False