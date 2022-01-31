class Solution:
    def merge(left, right):
        result = []
        i, j = 0, 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        while (i < len(left)):
            result.append(left[i])
            i += 1
        while (j < len(right)):
            result.append(right[j])
            j += 1

        return result 

    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) < 2:
            return nums[:]
        else:
            middle = len(nums) // 2
            left = self.sortArray(nums[:middle])
            right = self.sortArray(nums[middle:])
            return merge(left, right) 