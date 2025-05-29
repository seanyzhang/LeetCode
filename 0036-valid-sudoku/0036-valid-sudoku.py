class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        for i in range(9):
            for j in range(9):
                curr = board[i][j]
                if curr == '.': continue
                box = (i // 3) * 3 + (j // 3)

                if curr in rows[i] or curr in cols[j] or curr in boxes[box]:
                    return False
                
                rows[i].add(curr)
                cols[j].add(curr)
                boxes[box].add(curr)

        return True
                

