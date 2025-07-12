class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Brute Force Approach
        # Time Complexity: O((m+n)log(m+n))
        # Space Complexity: O(m+n)
        # nums1[m:] = nums2[:n] # humne nums1 ke last m elements ko nums2 ke n elements se replace kar diya (We replaced the last m elements of nums1 with the n elements of nums2)
        # nums1.sort() # phir humne nums1 ko sort kar diya (Then we sorted nums1)

        # Two Pointer Approach
        # Time Complexity: O(m+n)
        # Space Complexity: O(1)
        p1, p2 = m - 1, n - 1
        p3 = m + n - 1
        while p1 >=0 and p2 >= 0:
            if nums2[p2] > nums1[p1]:
                nums1[p3] = nums2[p2]
                p2 -= 1
            else:
                nums1[p3] = nums1[p1]
                p1 -= 1
            p3 -= 1
        while p2 >= 0:
            nums1[p3] = nums2[p2]
            p2 -= 1
            p3 -= 1
        # No need to handle p1 because if p1 is still >= 0, it means all elements of nums2 are already placed correctly in nums1.
        # If p1 < 0, it means nums1 already has all its elements in place.
        # Thus, we don't need to do anything further.