class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        ans = 0
        seen = {}

        i = 0
        for j in range(n):
            if s[j] in seen and seen[s[j]] >= i:
                i = seen[s[j]] + 1

            currLen = j - i + 1
            seen[s[j]] = j
            ans = max(currLen,ans)

        return ans
                
                
                    


