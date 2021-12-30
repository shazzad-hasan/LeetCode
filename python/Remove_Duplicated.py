class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        result = []
        for num in nums:
            if num in result:
                pass
            else:
                result.append(num)

        k = len(result)

        for i in range(k):
            nums[i] = result[i]

        return k