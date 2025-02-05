class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        final = 0
        G1 = 'VX'
        G2 = 'LC'
        G3 = 'DM'
        for i in range(len(s)):
            if s[i] == 'I':
                if i == len(s)-1:
                    final += 1
                elif s[i+1] in G1:
                    final -= 1
                else:
                    final += 1
            if s[i] == 'V':
                final += 5
            if s[i] == 'X':
                if i == len(s)-1:
                    final += 10
                elif s[i+1] in G2:
                    final -= 10
                else:
                    final += 10
            if s[i] == 'L':
                final += 50
            if s[i] == 'C':
                if i == len(s)-1:
                    final += 100
                elif s[i+1] in G3:
                    final -= 100
                else:
                    final += 100
            if s[i] == 'D':
                final += 500
            if s[i] == 'M':
                final += 1000
        return final