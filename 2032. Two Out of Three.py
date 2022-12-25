class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
            nums1 = set(nums1)
            nums2 = set(nums2)
            nums3 = set(nums3)
            x = set()
            for i in nums1:
                if i in nums2 or i in nums3:
                    x.add(i)
            for i in nums2:
                if i in nums3 or i in nums1:
                    x.add(i) 
            for i in nums3:
                 if i in nums2 or i in nums1:
                     x.add(i)
            return list(x)
