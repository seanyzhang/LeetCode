class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or numRows > len(s):
            return s
            
        def simulate(s, numRows):
            board = [ [None] for i in range(numRows)]
            row = 0
            direction = "down"
            for i in range(len(s)):
                if row == 0:
                    direction = "down"

                if direction == "down":
                    board[row].append(s[i])
                    if row < numRows - 1:
                        row += 1

                if direction == "diagonal":
                    for line in range(numRows):
                        if line != row:
                            board[line].append(None)
                        else:
                            board[row].append(s[i])
                            row -= 1

                if row == numRows - 1:
                    direction = "diagonal"
            
            fin = ""
            for line in range(numRows):
                curr = "".join([x for x in board[line] if x is not None])
                fin += curr
            
            
            return fin

        x = simulate(s, numRows)
        return x
                
