class Solution(object):
    def numPairsDivisibleBy60(self, time):
        """
        :type time: List[int]
        :rtype: int
        """
        c = defaultdict(int)
        for t in time:
            c[t % 60] += 1
        
        total = 0

        if c[0]:
            total += c[0] * (c[0] - 1) // 2
        
        if c[30]:
            total += c[30] * (c[30] - 1) // 2
       
        for val in range(1,30):
            complement = 60 - val
            total += c[val] * c[complement]


        return total