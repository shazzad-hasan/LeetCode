class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            sign = -1
        else:
            sign = 1 
        x = sign * x
        
        MIN = -2147483648 # -2^31
        MAX = 2147483647 # 2^31-1
        
        rev_num = 0
        
        while x != 0: 
            # pop operation
            digit = x % 10
            x =  x // 10
            
            # check overflow
            if (rev_num > MAX // 10 or (rev_num == MAX // 10 and digit >= MAX % 10)):
                return 0
            elif (rev_num < MIN // 10 or (rev_num == MIN // 10 and digit <= MIN % 10)):
                return 0
            
            else:
            # push operation
                rev_num = rev_num * 10 + digit
        return sign * rev_num 
        