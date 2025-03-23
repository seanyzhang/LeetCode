class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, k):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type k: int
        :rtype: int
        """
        itin = {}
        reached = False
        for start, end, cost in flights:
            if start not in itin:
                itin[start] = set([(end,cost)])
            else:
                itin[start].add((end,cost))

            if end not in itin:
                itin[end] = set()
            
            if end == dst:
                reached = True
        
        if src not in itin or not reached:
            return -1
            
        seen = {}
        heap = [(0,-1,src)]
        while heap:
            cost, stops, curr = heapq.heappop(heap)
            
            if curr == dst and stops <= k:
                return cost

            if curr not in seen or seen[curr] > stops:
                seen[curr] = stops
                for newDest,price in itin[curr]:
                    heapq.heappush(heap,(cost + price, stops + 1, newDest))
        return -1
        