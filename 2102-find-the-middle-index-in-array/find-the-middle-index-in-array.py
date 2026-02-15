class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        prefix = [0]
        for x in nums:
            prefix.append(prefix[-1] + x)

        total = prefix[-1]

        for i in range(len(nums)):
            left = prefix[i]
            right = total - prefix[i+1]
            if left == right:
                return i

        return -1