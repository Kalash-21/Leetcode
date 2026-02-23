class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        total = 0
        l = 0
        mini = float('inf')

        for r in range(len(nums)):
            total += nums[r]

            while total >= target:
                mini = min(mini, r - l + 1)
                total -= nums[l]
                l += 1

        return 0 if mini == float('inf') else mini