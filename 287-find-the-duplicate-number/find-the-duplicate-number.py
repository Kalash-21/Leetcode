class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for num in nums:
            current = abs(num)
            index = current - 1

            if nums[index] < 0:
                return current
            else:
                nums[index] = nums[index] * -1