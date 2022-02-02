class Solution:
    def mySqrt(self, x: int) -> int:
        low = 1
        high = x
        while low <= high:
            ans = (high+low)//2
            if ans**2 > x:
                high = ans -1
            else:
                low = ans + 1
        return high