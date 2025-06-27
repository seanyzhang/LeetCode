class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        d = defaultdict(list)
        for word in strs:
            c = Counter(word)
            key = frozenset(c.items())
            d[key].append(word)
        
        return list(d.values())
           
