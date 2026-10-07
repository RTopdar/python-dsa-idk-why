def findMedianSortedArrays( nums1: list[int], nums2: list[int]) -> float:
        merged = sorted(nums1+nums2)
        n = len(merged)
        return(merged[n//2] if n % 2 != 0 else (merged[n//2] + merged[(n//2)-1]) / 2)
        
