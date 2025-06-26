class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        sCounter = Counter(s)
        tCounter = Counter(t)

        if sCounter != tCounter:
            return False
        
        return True