class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        a=[-1]*(len(nums)+1)
        for num in nums:
            if a[num]!=-1:
                return num
            else:
                a[num]=0
            