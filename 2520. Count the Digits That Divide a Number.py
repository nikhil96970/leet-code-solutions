class Solution:
    def countDigits(self, num: int) -> int:
        cnt = 0
        tmp = num
        while tmp:   
            if num % (tmp % 10) == 0:
                cnt += 1
            tmp //= 10
        return cnt

        
