class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        first = 0
        last = len(nums) -1
        
        while first <= last:
            mid = (first+last) // 2
            if nums[mid] == target:
                return mid
            else:
                if nums[mid] > target:
                    last = mid - 1
                else:
                    first = mid + 1
            
        return first