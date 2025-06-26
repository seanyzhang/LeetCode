class Solution(object):
    def maxProbability(self, n, edges, succProb, start_node, end_node):
        """
        :type n: int
        :type edges: List[List[int]]
        :type succProb: List[float]
        :type start_node: int
        :type end_node: int
        :rtype: float
        """
        adj = {}

        for i in range(len(edges)):
            st = edges[i][0]
            end = edges[i][1]
            if succProb[i] == 0:
                continue

            prob = -math.log(succProb[i]) 
            
            if st not in adj:
                adj[st] = []  
            adj[st].append([prob, end])
            if end not in adj:
                adj[end] = []
            adj[end].append([prob, st])
        
        if start_node not in adj: 
            return 0.0

        heap = [[0, start_node]]
        seen = set()

        while heap:
            prob, node = heappop(heap)

            if node in seen:
                continue 
            
            seen.add(node)

            if node == end_node:
                return math.exp(-prob)

            if node in adj: 
                for nextProb, nextNode in adj[node]:
                    newProb = prob + nextProb
                    heappush(heap, [newProb, nextNode])
        
        return 0.0