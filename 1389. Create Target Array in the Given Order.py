class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        length = len(nums)
        target = []
        for i in range(length):
            if index[i] >= len(target): target.append(nums[i])
            else: target.insert(index[i], nums[i])
        return target
