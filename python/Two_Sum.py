class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        size = len(nums)
        summa = 0
        for i in range(size-1):
            for j in range(i+1, size):
                summa = nums[i] + nums[j]
                if summa == target:
                    return [i, j]
