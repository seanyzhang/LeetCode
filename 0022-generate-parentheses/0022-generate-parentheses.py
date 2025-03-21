class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        return self.generate(n)
        
    
    def generate(self, n, s = None, curr = 1):
        if curr == 1:
            s = ["()"]
        
        if curr == n:
            return s

        else:
            new = set()
            for x in s:
                for i in range(len(x)):
                    y = x[:i] + "()" + x[i:]
                    new.add(y)
            
            return self.generate(n, list(new), curr + 1)

            






            



            