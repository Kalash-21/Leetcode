class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # nums=sorted(nums)
        # return nums[len(nums)//2]
        a = {}
        n = len(nums)

        for num in nums:
            if num in a:
                a[num] += 1
            else:
                a[num] = 1

            if a[num] > n // 2:
                return num