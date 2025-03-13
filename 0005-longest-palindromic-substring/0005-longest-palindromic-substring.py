class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        start = False
        longest = s[0]
        for i in range(len(s)):

            curr = self.check(s, i, i)
            curr2 = self.check(s, i , i + 1)
            longest = max(longest, curr, curr2, key = len)

        return longest

    def check(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            
            l -= 1
            r += 1

        return s[l+1:r]





