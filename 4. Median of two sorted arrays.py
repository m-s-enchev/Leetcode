from enum import unique


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        nums1.extend(nums2)
        new_list = sorted(nums1)
        result = 0
        if len(new_list)%2 == 0:
            index = len(new_list)/2-1
            result = (float(new_list[index]) + float(new_list[index+1]))/2
        else:
            result = new_list[len(new_list)//2]
        return result


new_sol = Solution()
print(new_sol.findMedianSortedArrays([1,2], [3,4]))
