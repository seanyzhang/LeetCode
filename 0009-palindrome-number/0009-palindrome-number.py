class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x is not str:
            x = str(x)
        for i in range(len(x)//2):
            if x[i] != x[-i-1]:
                return False
        return True
        