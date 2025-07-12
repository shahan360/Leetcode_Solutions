class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Brute Force Approach
        # Time Complexity: O((m+n)log(m+n))
        # Space Complexity: O(m+n)
        nums1[m:] = nums2[:n] # humne nums1 ke last m elements ko nums2 ke n elements se replace kar diya (We replaced the last m elements of nums1 with the n elements of nums2)
        nums1.sort() # phir humne nums1 ko sort kar diya (Then we sorted nums1)