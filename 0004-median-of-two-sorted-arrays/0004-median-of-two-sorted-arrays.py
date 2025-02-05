class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        itcount = 0

        while True:
            if nums1 and nums2:
                curr = min(nums1[0],nums2[0]) 
                nums1.remove(curr) if curr == nums1[0] else nums2.remove(curr)
            else:
                if nums1:
                    curr = nums1[0]
                    nums1.remove(curr)
                else:
                    curr = nums2[0]
                    nums2.remove(curr)
                
            itcount += 1
            totalLen = len(nums1) + len(nums2)

            if itcount == totalLen:
                if nums1 and nums2:
                    n = min(nums1[0],nums2[0])
                else:
                    if nums1:
                        n = nums1[0]
                    else:
                        n = nums2[0]
                return (curr + n) / 2.0
            
            if itcount > totalLen:
                return curr
        

            
        
