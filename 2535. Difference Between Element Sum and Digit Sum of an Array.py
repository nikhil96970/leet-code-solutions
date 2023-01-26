class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        s1=sum(nums)
        s2=0
        for i in nums:
            n=i
            while(n>0):
                s2+=n%10
                n=n//10
        return abs(s2-s1)
