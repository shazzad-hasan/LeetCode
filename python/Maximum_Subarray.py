class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        l = len(nums)
        # create an empty list
        subarray_sums = [None]*l
        subarray_sums[0] = nums[0] # since subarray must be nonempty
        
        # Kadane's algorithm
        for i in range(1, l):
            subarray_sums[i] = max(nums[i], nums[i] + subarray_sums[i-1])
        
        return max(subarray_sums)