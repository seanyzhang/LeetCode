class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        left, top, right, bottom = 0,0,0,0 # bounds
        direction = 'r'
        ans = []
        r,c = 0,0

        while len(ans) < len(matrix) * len(matrix[0]):
            ans.append(matrix[r][c])

            if direction == 'r':
                if c + 1 == len(matrix[0]) - right:
                    direction = 'd'
                    top += 1
                    r += 1
                else:
                    c += 1

            elif direction == 'd':
                if r + 1 == len(matrix) - bottom:
                    direction = 'l'
                    right += 1
                    c -= 1
                else:
                    r += 1

            elif direction == 'l':
                if c == left:
                    direction = 'u'
                    bottom += 1
                    r -= 1
                else:
                    c -= 1

            elif direction == 'u':
                if r == top:
                    direction = 'r'
                    left += 1
                    c += 1
                else:
                    r -= 1
        
        return ans



        