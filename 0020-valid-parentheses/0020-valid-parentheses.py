class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        if len(s) == 0:
            return False

        respective = {
            ")": "(",
            "}": "{",
            "]": "["
        }

        dq = deque()
        for char in s:
            if char in respective.keys():
                if not dq:
                    return False
                else:
                    prev = dq[-1]
                    if prev != respective[char]:
                        return False
                    else:
                        dq.pop()
            
            else:
                dq.append(char)
        
        if len(dq) != 0:
            return False

        return True
