class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        d = board
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)] 
        nums = set(str(i) for i in range(1,10))

        for i in range(9):
            for j in range(9):
                curr = board[i][j]
                if curr == '.': continue
                box = (i // 3) * 3 + (j // 3)              
                rows[i].add(curr)
                cols[j].add(curr)
                boxes[box].add(curr)
        
        def backtrack(r, c):
            if r == 9: return True
            curr = board[r][c]
            if curr != ".": return backtrack(r,c+1) if c < 8 else backtrack(r+1,0)

            box = (r // 3) * 3 + (c // 3)
            possible = nums - rows[r] - cols[c] - boxes[box]
            for num in possible:
                board[r][c] = num
                rows[r].add(num)
                cols[c].add(num)
                boxes[box].add(num)

                if c < 8:
                    if backtrack(r, c + 1):
                        return True
                else:
                    if backtrack(r + 1, 0):
                        return True
                
                board[r][c] = "."
                rows[r].remove(num)
                cols[c].remove(num)
                boxes[box].remove(num)

            return False

        backtrack(0,0)
        return board


