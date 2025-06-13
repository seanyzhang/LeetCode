class Solution(object):
    def rotateTheBox(self, boxGrid):
        """
        :type boxGrid: List[List[str]]
        :rtype: List[List[str]]
        """
        m = len(boxGrid)
        n = len(boxGrid[0])

        for row in boxGrid:
            lastObst = len(row) - 1
            for curr in range(len(row) - 1, -1, -1):
                if row[curr] == "*":
                    lastObst = curr - 1
                elif row[curr] == "#":
                    if curr != lastObst:
                        row[lastObst], row[curr] = row[curr], '.'
                    lastObst -= 1

        newMatrix = [["."] * m for _ in range(n)]

        for i in range(m):
            for j in range(n):
                newMatrix[j][m-i-1]= boxGrid[i][j]
        
        return newMatrix

    

        