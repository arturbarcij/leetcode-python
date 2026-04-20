class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        # pairs (i, j)
        # 0 <= j < nums2.length
        # if i <= j and nums1[i] <= nums2[j]
        # distance j - i
        # return max distance of (i, j) else return 0