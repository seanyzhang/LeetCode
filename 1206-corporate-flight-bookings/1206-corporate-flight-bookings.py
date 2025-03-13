class Solution(object):
    def corpFlightBookings(self, bookings, n):
        """
        :type bookings: List[List[int]]
        :type n: int
        :rtype: List[int]
        """
        
        times = [0] * (n + 1)
        for lidx, ridx, val in bookings:
            times[lidx - 1] += val
            times[ridx] -= val
        
        ans = []
        ac = 0
        for i in range(len(times) - 1):
            ac += times[i]
            ans.append(ac)
        
        return ans