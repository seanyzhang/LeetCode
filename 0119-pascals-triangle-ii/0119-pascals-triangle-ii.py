class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        ans = [1]
        num, den = rowIndex, 1
        while len(ans) < rowIndex // 2 + 1:
            nx = ans[-1] * num / den
            ans.append(nx)
            num -= 1
            den += 1

        if rowIndex % 2 == 1:
            return ans + ans[::-1]
        else:
            return ans + ans[:-1][::-1]