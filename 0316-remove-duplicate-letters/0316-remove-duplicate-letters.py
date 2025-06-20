class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        counter = Counter(s)
        stack = []
        seen = set()

        for char in s:
            counter[char] -= 1
            if char in seen:
                continue
            
            while stack and char < stack[-1] and counter[stack[-1]] > 0:
                removed = stack.pop()
                seen.remove(removed)
                
            stack.append(char)
            seen.add(char)

        return "".join(stack)