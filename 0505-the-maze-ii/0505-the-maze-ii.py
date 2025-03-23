class Solution(object):
    def shortestDistance(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: int
        """
        visited = {} 
        directions = ['up', 'down', 'left', 'right']
        heap = [(0,tuple(start))]

        while heap:
            dist, point = heapq.heappop(heap)
            
            if point == tuple(destination):
                return dist

            if point not in visited or dist < visited[point]:
                visited[point] = dist
                for direction in directions:
                    delta, r, c = self.roll(maze, point, direction)
                    heapq.heappush(heap,(dist + delta, tuple([r,c])))

        return -1

    def roll(self, maze, start, direction):
        [r, c] = start
        delta = 0
        if direction == 'up':
            while r > 0 and maze[r - 1][c] != 1:
                delta += 1
                r -= 1

        if direction == 'down':
            while r < len(maze) - 1 and maze[r + 1][c] != 1:
                delta += 1
                r += 1

        if direction == 'left':
            while c > 0 and maze[r][c - 1] != 1:
                delta += 1
                c -= 1

        if direction == 'right':
            while c < len(maze[0]) - 1 and maze[r][c + 1] != 1:
                delta += 1
                c += 1

        return delta, r, c
        