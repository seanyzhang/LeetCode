class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []

        letters = {'2': set(['a','b','c']), '3': ['d','e','f'], '4': ['g','h','i'], '5': ['j','k','l'], '6': ['m','n','o'], '7': ['p','q','r','s'],
          '8': ['t','u','v'], '9': ['w','x','y','z']}
        fin = []
        curr = []
        dig = list(digits)

        for digit in dig:
            if not fin:
                fin = [ch for ch in letters[digit]]
            else:
                for y in fin:
                    ylength = len(y)
                    for ch in letters[digit]:
                        new = y + ch
                        curr.append(new)
                fin = curr
                curr = []

        return fin
