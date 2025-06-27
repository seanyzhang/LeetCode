class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        d = defaultdict(list)
        for word in strs:
            key = "".join(sorted(word))
            d[key].append(word)
        
        return list(d.values())
           
