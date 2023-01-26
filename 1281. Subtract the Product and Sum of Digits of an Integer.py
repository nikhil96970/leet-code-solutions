class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product=1
        sum=0
        num=str(n)
        for i in num:
            product= product*int(i)
            sum=sum+int(i)
        return product-sum
