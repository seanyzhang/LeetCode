class Solution(object):
    def betterCompression(self, compressed):
        """
        :type compressed: str
        :rtype: str
        """
        seen = {}
        i = 0
        ch, fre = "" , ""
        while i < len(compressed):
            if compressed[i].isalpha():
                if ch:
                    if ch in seen:
                        seen[ch] = ch + str(int(seen[ch][1:]) + int(fre))
                    else:
                        seen[ch] = ch + fre
                    fre = ""
                ch = compressed[i]
                i += 1
            else:
                fre += compressed[i]
                i += 1
        
        if ch:
            if ch in seen:
                seen[ch] = ch + str(int(seen[ch][1:]) + int(fre))
            else:
                seen[ch] = ch + fre

        
        x = list(seen.values())
        x.sort(key = lambda k: k[0])
        return "".join(x)