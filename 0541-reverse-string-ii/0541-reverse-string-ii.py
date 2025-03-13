class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        idxs = range((len(s) // k )+ 1) if len(s) > k else [0]
            
        ans = s

        for idx in idxs:
            if idx % 2 == 1:
                continue

            x = idx * k
            bef, aft = ans[:x] , ans[x+k:]
            curr = ans[x:x+k]
            curr = curr[::-1]

            ans = bef + curr + aft

        return ans