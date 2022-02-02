class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        first = 0
        last = len(arr)-1
        while first < last:
            mid = (first+last) // 2
            if arr[mid-1] < arr[mid] > arr[mid+1]:
                return mid
            elif arr[mid] < arr[mid+1]:
                first = mid + 1
            else:
                last = mid - 1
        return first