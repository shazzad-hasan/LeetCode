class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        first = 0
        last = len(nums)-1
        while first < last:
            mid = (first+last) // 2
            if nums[mid-1] < nums[mid] and nums[mid] > nums[mid+1]:
                return mid
            elif nums[mid] < nums[mid+1]:
                first = mid + 1
            else:
                last = mid - 1
        return first