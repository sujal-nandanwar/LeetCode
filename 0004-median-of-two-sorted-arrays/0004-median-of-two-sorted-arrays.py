
class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        arr=[]
        left=0
        right=0
        while left<len(nums1) and right<len(nums2):
            if nums1[left]<nums2[right]:
                arr.append(nums1[left])
                left+=1
            else:
                arr.append(nums2[right])
                right+=1
        while left<len(nums1):
            arr.append(nums1[left])
            left+=1
        while right<len(nums2):
            arr.append(nums2[right])
            right+=1
        var = len(arr)
        if var%2==0:
            return (arr[var // 2-1] + arr[var // 2]) / 2
        else:
            return float(arr[var//2])
 