class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1: return "1"

        return self.count(self.countAndSay(n-1))

    def count(self,n):
        N = str(n)
        ans = ""
        lastDigit = "."
        for i in range(len(N)):
            if N[i] == lastDigit:
                q = str(int(ans[-2]) + 1)
                ans = ans[:-2] + q + ans[-1]
            else:
                ans += "1" + N[i]
                lastDigit = N[i]
        
        return ans