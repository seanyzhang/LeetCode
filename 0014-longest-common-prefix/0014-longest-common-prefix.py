class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        fin = ""

        i = 0 
        lengths = [len(string) for string in strs]

        while i < min(lengths):
            curr = strs[0][i]
            for string in strs:
                if string[i] != curr:
                    return fin
            fin += curr
            i += 1
                
        return fin
        