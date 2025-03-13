class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        final = ""
        neg = False

        s = s.strip()

        if not s:
            return 0
        
        i = 0

        if not s[i].isdigit():
            if s[i] == "-":
                neg = True
            elif s[i] not in "+-":
                return 0
            i += 1
        
        while i < len(s) and s[i].isdigit():
            final += s[i]
            i += 1

        if not final:
            return 0
            
        intfinal = int(final)
        
        if neg == True:
            intfinal *= -1
        if intfinal < - (2 ** 31):
            return - (2 ** 31)
        elif intfinal > (2 ** 31) - 1:
            return (2 ** 31) - 1
        
        return intfinal
